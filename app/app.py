# import flask
from flask import Flask, render_template, request, jsonify
import quandl
import pandas as pd

# # app Flask
# -----------------------------------------------------|
app = Flask(__name__)


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

		return render_template('simple.html',  tables=[df.to_html(classes='data', header="true")])



# run the server
if __name__ == '__main__':
    app.run(debug=True)

# boom!