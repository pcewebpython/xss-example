""" script main.py """

# imports
import os
import base64
import html
import random

from peewee import IntegrityError
from werkzeug.exceptions import HTTPException
from flask import Flask, request, session
from model import Message
# -------------------------------------------

APP = Flask(__name__)
APP.secret_key = b"\xe0\x95\xf2`W8'X,2\xfc\x88Z\x8c\x97\xad~1\xd8k\xbb\xaf\xd7\xab"
#APP.secret_key = os.environ.get('SECRET_KEY').encode()
# -------------------------------------------

@APP.route("/", methods=["GET", "POST"])
def home():
    """ home """
    if "csrf_token" not in session:
        session["csrf_token"] = str(random.randint(10000000, 99999999))

    if request.method == "POST":
        if request.form.get("csrf_token", None) == session["csrf_token"]:
            try:
                msg = Message(content=request.form["content"])
                msg.save()
            except (HTTPException, IntegrityError) as err:
                print("no message inserted: ", err)
        else:
            raise RuntimeError("Possible CSRF attack")
    # -------------------------------------------

    body = """
<html>
<body>
<h1>Class Message Board</h1>
<h2>Contribute to the Knowledge of Others</h2>
<form method="POST">
    <textarea name="content"></textarea>
    <input type="hidden" name="csrf_token" value="{}">
    <input type="submit" value="Submit">
</form>

<h2>Wisdom From Your Fellow Classmates</h2>
""".format(session["csrf_token"])
    # -------------------------------------------

    for msg in Message.select():
        body += """
<div class="message">
{}
</div>
""".format(html.escape(msg.content.strip(), quote=True))

    # format(msg.content.replace("<", "&lt;").replace(">", "&gt;")
    #           .replace("&", "&amp;")).replace("'", "&#x27"))
    #           .replace ('"', "&quot;"))
    return body


# ===========================================
if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 6738))
    APP.run(host="0.0.0.0", port=PORT)
