from flask import Flask
import json

j = ['aj' , 'ab'] 
app = Flask(__name__)
@app.route('/j' , methods = ["GET"])
def homepage():
    return json.dumps(j) 

if __name__ == '__main__':
    app.run()