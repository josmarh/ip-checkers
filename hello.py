from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
   return 'Hello World'

# method 2 routing
def hello(name):
   return 'you are go to go %s!' % name
app.add_url_rule('/<name>', 'hellos', hello)

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)