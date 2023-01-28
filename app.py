import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        name = request.form["name"]
        degree = request.form["degree"]
        university = request.form["university"]
        job = request.form["job"]
        company = request.form["company"]

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(name,degree,university,job,company),
            temperature=0.6,
            max_tokens=300,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(name,degree,university,job,company):
    return """Generate a cover letter for {} who is a {} 
    graduate from {} applying for the position of {} in the company {} 
    """.format(name,degree,university,job,company)
