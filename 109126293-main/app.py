from flask import Flask, render_template, request
import rp_calculator

app = Flask('__name__')


@app.route("/")
def index():

    return render_template("index.html")

@app.route("/greet", methods=['GET'])
def greet():
    username = request.args.get("username")
    return render_template("greet.html", username = username)

@app.route("/subjects", methods=['GET'])
def subjects():
    return render_template("subjects.html")

@app.route("/rp", methods=['GET'])
def rp():
    return render_template("rp.html")

@app.route("/result", methods=['GET'])
def result():
    grades = request.args.to_dict()
    result = rp_calculator.rp_calculator(grades)
    print(result)
    return render_template("result.html", result = result)
