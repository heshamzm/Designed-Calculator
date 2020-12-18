from flask import Flask, render_template, url_for, request, redirect
import math

app = Flask(__name__)               


@app.route("/", methods=["GET", "POST"])
def calc():

    return render_template('calc.html')