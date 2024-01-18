from flask import Flask
# Flask.preprocess_request = 4000
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! from the Python side'
@app.route('/test')
def test():
    return "python Get Api Testing, success 1"
@app.route('/abhay')
def abhay():
    return "Hello Abhay Sir ...testing python api was processed !"
if __name__ == '__main__':
    app.run(debug=True,port=4200)
