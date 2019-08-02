""" Super basic flask message board """
import os
import html
from flask import Flask, request, render_template
from model import Message


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """ View for Message board home page """
    if request.method == "POST":
        Message(content=html.escape(request.form["content"]).strip("'")).save()

    results = [msg.content for msg in Message.select().execute()]
    return render_template("template.jinja2", messages=results)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host="0.0.0.0", port=port)
