from flask import Flask , render_template

j = ['aj' , 'ab'] 
app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template('app.json')

if __name__ == '__main__':
    app.run()