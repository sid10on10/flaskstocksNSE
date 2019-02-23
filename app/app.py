# import flask
from flask import Flask, render_template, request, Response
import quandl
import pandas as pd
import plotly
import plotly.graph_objs as go
import json
import numpy as np


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
		#new_df = df.reset_index()
		xScale = df['Close']
		yScale = df['Open']

		# Create a trace
		trace = go.Scatter(
	    	x = xScale,
	    	y = yScale
			)

		data = [trace]
		
		graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    	
		return render_template('simple.html',  tables=[df.to_html(classes='data', header="true")], graphJSON=graphJSON)



# run the server
if __name__ == '__main__':
    app.run(debug=True)

# boom!