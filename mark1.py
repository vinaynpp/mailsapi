import yagmail
import keyring

contents = []


def bhejo(meraemail, merapswd, email, subject, contents):
    print("")
    print("LET'S START")

    yagmail.register(meraemail, merapswd)

    print("")
    print("loggedin")

    with yagmail.SMTP(meraemail, 'oauth2_creds.json') as yag:
        yag.send(email, subject, contents)

    print("")
    print("TASK SUCCESSFULLY COMPLETED")
