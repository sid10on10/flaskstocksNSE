# import flask
from flask import Flask, render_template, request, Response
import quandl
import pandas as pd
import matplotlib  
matplotlib.use('TkAgg')   
import matplotlib.pyplot as plt, mpld3
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from io import BytesIO


# # app Flask
# -----------------------------------------------------|
app = Flask(__name__)
quandl.ApiConfig.api_key = "VKXmKjxxSpX-ydXye9mu"


@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		#request was a POST
		ticker = request.form['company'].upper()
		start_date = request.form['start_date']
		end_date = request.form['end_date']
		data = quandl.get("NSE/{}".format(ticker), start_date=start_date, end_date=end_date)
		df = pd.DataFrame(data)
		#image = df['Close'].plot(legend=True,figsize=(10,4))
		Y = df['Close']
		plot_1 = plt.plot(Y)
		# Let's go ahead and plot out several moving averages
		plot_2 = Y.rolling(window=20, center=False).mean().plot(legend=True,figsize=(10,4))
		text= mpld3.fig_to_html(plot_1)
		text2 = mpld3.fig_to_html(plot_2)

	


		return render_template('simple.html',  tables=[df.to_html(classes='data', header="true")], html=text, html2=text2)



# run the server
if __name__ == '__main__':
    app.run(debug=True)

# boom!