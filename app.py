from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/hello")
def hello_world():
    return "<p>Hello world, this is Flask</p>"

@app.route("/products")
def hello_products():
    return "<p>Hello, this is products page</p>"

@app.route("/about")
def about():
    return "<p>Hello, this is About us page</p>"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)