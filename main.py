import base64
import os
import random

from flask import Flask, request, session

from model import Message

app = Flask(__name__)
app.secret_key = b'\x9d\xb1u\x08%\xe0\xd0p\x9bEL\xf8JC\xa3\xf4J(hAh\xa4\xcdw\x12S*,u\xec\xb8\xb8'

@app.route('/', methods=['GET', 'POST'])
def home():

    if 'csrf_token' not in session:
        session['csrf_token'] = str(random.randint(10000000, 99999999))

    if request.method == 'POST':
        if request.form.get('csrf_token', None) == session['csrf_token']:
            m = Message(content=request.form['content'])
            m.save()

    body = """
<html>
<body>
<h1>Class Message Board</h1>
<h2>Contribute to the Knowledge of Others</h2>
<form method="POST">
    <input type="hidden" name="csrf_token" value="{}">

    <textarea name="content"></textarea>
    <input type="submit" value="Submit">
</form>

<h2>Wisdom From Your Fellow Classmates</h2>
""".format(session['csrf_token'])
    
    for m in Message.select():
        body += """
<div class="message">
{}
</div>
""".format(m.content.replace('<', '&lt;').replace('>', '&gt;'))

    return body 


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

