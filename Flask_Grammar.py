import os

from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI
client = OpenAI(
    api_key=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,
)

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        texts = request.form["texts"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.6,max_tokens=64, top_p=1,
            messages=[
                {"role": "system","content": "Students will provide you with an English text that needs to be revised. Please revise the grammar and logic of the accepted text."},
                {"role": "user", "content": texts}
            ]
        )
        return redirect(url_for("index", result=response.choices[0].message.content))

    result = request.args.get("result")
    return render_template("Grammar V2.html", result=result)
