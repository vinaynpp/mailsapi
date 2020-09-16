import os

import mark1

from flask import Flask, request, jsonify, render_template

from checknaka import dekh

app = Flask(__name__, template_folder='templates', static_folder='static')




@app.route('/portal/', methods=['GET', 'POST'])
def takeform():
    if request.method == 'GET':
        return render_template('portal.html')
    name = request.form['name']
    # Retrieve the name from url parameter
    meraemail = request.form['meraemail']
    merapswd = request.form['merapswd']
    email = request.form['email']
    subject = request.form['subject']
    contents = request.form['contents']

    # For debugging

    print(f"got name {name}")
    print(f"got meraemail {meraemail}")
    print(f"got merapswd {merapswd}")
    print(f"got email {email}")
    print(f"got subject {subject}")
    print(f"got contents {contents}")

    response = {}
    response["name"] = f'{dekh(name)}'
    response["meraemail"] = f'{dekh(meraemail)}'
    response["merapswd"] = f'{dekh(merapswd)}'
    response["email"] = f'{dekh(email)}'
    response["subject"] = f'{dekh(subject)}'
    response["contents"] = dekh(contents)

    # Check if user sent a name at all
    if not meraemail:
        response["ERROR"] = "no password found, please send a password."
    # Check if the user entered a number not a name
    elif str(email).isdigit():
        response["ERROR"] = f"{email}can't be numeric."
    # Now the user entered a valid name
    else:
        mark1.bhejo(meraemail, merapswd, email, subject, contents)

        response["MESSAGE"] = f"Welcome {meraemail} with password {merapswd} to our awesome platform!!"

    # Return the response in json format

    return jsonify(response)


@app.route('/json/', methods=['GET', 'POST'])
def takejson():
    name = request.args.get("name", None)
    meraemail = request.args.get("meraemail", None)
    merapswd = request.args.get("merapswd", None)
    email = request.args.get("email", None)
    subject = request.args.get("subject", None)
    contents = request.args.get("contents", None)

    # For debugging

    print(f"got name {name}")
    print(f"got meraemail {meraemail}")
    print(f"got merapswd {merapswd}")
    print(f"got email {email}")
    print(f"got subject {subject}")
    print(f"got contents {contents}")

    response = {}
    response["name"] = f'{dekh(name)}'
    response["meraemail"] = f'{dekh(meraemail)}'
    response["merapswd"] = f'{dekh(merapswd)}'
    response["email"] = f'{dekh(email)}'
    response["subject"] = f'{dekh(subject)}'
    response["contents"] = dekh(contents)

    # Check if user sent a name at all
    if not meraemail:
        response["ERROR"] = "no password found, please send a password."
    # Check if the user entered a number not a name
    elif str(email).isdigit():
        response["ERROR"] = f"{email}can't be numeric."
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
