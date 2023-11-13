from flask import Flask, render_template, request


panel = Flask(__name__) # initializng the flask app


@panel.route('/')
def helloworld():
    return render_template("index.html")

if __name__ == '__main__':
    panel.run(debug = False, port = 9000)