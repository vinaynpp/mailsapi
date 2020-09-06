import os
import time

import yagmail
import keyring

import mark1

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter

    username = request.args.get("username", None)
    meraemail = request.args.get("meraemail", None)
    merapswd = request.args.get("merapswd", None)
    email = request.args.get("email", None)
    subject = request.args.get("subject", None)
    contents = request.args.get("contents", None)

    # For debugging
    print(f"got name {username}")
    print(f"got name {meraemail}")
    print(f"got name {merapswd}")
    print(f"got name {email}")
    print(f"got name {subject}")
    print(f"got name {contents}")

    response = {}

    # Check if user sent a name at all
    if not meraemail:
        response["ERROR"] = "no password found, please send a password."
    # Check if the user entered a number not a name
    elif str(email).isdigit():
        response["ERROR"] = "{email}can't be numeric."
    # Now the user entered a valid name
    else:
        mark1.bhejo(meraemail, merapswd, email, subject, contents)

        response["MESSAGE"] = f"Welcome {meraemail} with password {merapswd} to our awesome platform!!"

    # Return the response in json format

    return jsonify(response)


@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('contents')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the
    # POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome  to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD": "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run()
    app.debug = True
    app.run()
    app.run(threaded=True, port=port, debug=True)
