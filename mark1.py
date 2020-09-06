import yagmail

contents = []


def bhejo(meraemail, merapswd,email, subject, contents ):
    print("")
    print("LET'S START")

    yagmail.register(meraemail, merapswd)

    print("")
    print("loggedin")

    with yagmail.SMTP(meraemail) as yag:
        yag.send(email, subject, contents)

    print("")
    print("TASK SUCCESSFULLY COMPLETED")
