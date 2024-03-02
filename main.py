import os
from flask import Flask, render_template

app = Flask(__name__)


def get_fact():
    return 'my_fact'


def pig_latinize(fact):
    return 'pig_latin_response', 'pig_latin_url'


@app.route('/')
def home():
    fact = get_fact()
    pig_latin_fact, pig_latin_url = pig_latinize(fact)
    return render_template('home.html', fact=fact, pig_latin_fact=pig_latin_fact,
                           pig_latin_url=pig_latin_url)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)