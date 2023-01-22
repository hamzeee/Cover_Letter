import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        name = request.form["name"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(name),
            temperature=0.6,
            max_tokens=300,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(name):
    return """Generate a cover letter for a mechanical engineer {} in the
    automotive industry who is looking to apply to the company Toyota for the
    position of Manufacturing Specialist
    """.format(name)
