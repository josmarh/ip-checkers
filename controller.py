from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')


@app.route('/search',methods = ['GET'])
def ipSearch():
   search = request.args.get('ipaddress')
   if(search != ''):
      url = 'https://api.ipgeolocation.io/ipgeo?apiKey=xxxxxxxxxxxxxxxxxxxxxxxxxx&ip='+search
      data = '{ "ip":search }'
      headers = {
         'Content-Type': 'application/json; charset=utf-8',
         'cache-control': "no-cache"
      }
   
      response = requests.request("GET", url, data=data, headers=headers)

      return render_template('index.html', res = response.json(), ipadd=search)
   else:
      return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)