from flask import Flask, jsonify
import json
import requests 
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


# Get exchange rate
@app.route('/exchange')
def get_exchange_rate():
	url='https://api.exchangeratesapi.io/latest'
	country_codes={'cc1':'ISK', 'cc2':'USD'}
	params={'base': '{}'.format(country_codes.get('cc1'))}
	r=requests.get(url,params=params)
	return jsonify(r.json().get('rates').get(country_codes["cc2"]))





if __name__ == '__main__':
    app.run(debug=True)