import time
from mark1 import bhejo

from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
    return 'hellllooooooo'
if __name__ =='__main__':
    app.run()