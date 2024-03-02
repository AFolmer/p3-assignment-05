import os
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    fact = 'myfact'
    pig_latin_fact = 'pig latin fact'
    pig_latin_url = 'pig latin url'
    return render_template('home.html', fact=fact, pig_latin_fact=pig_latin_fact,
                           pig_latin_url=pig_latin_url)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)