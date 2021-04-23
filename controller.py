from flask import Flask, render_template, jsonify, request,redirect
import requests
app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')


@app.route('/search',methods = ['GET'])
def ipSearch():
   search = request.args.get('ipaddress')
   url = 'https://api.ipgeolocation.io/ipgeo?apiKey=a5bb47955e2547f38ead40538034b5ae'
   data = '{ "ip":search }'
   headers = {
      'Content-Type': 'application/json; charset=utf-8',
      'cache-control': "no-cache"
    }
   
   response = requests.request("GET", url, data=data, headers=headers)

   return render_template('index.html', res = response.text, ipadd=search)


if __name__ == '__main__':
    app.run(debug = True)