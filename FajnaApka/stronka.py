from flask import Flask, render_template

stronka = Flask (__name__)


@stronka.route('/')
def index():
    return render_template('index.html')
stronka.run(debug=True)