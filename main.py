import os
import time
from mark1 import bhejo

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hellllooooooo'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run()
    app.debug=True
    app.run()
    app.run(port=port, debug=True)
