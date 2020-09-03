import yagmail
import csv

print("")
print("LET'S START")
print("")
meraemail = str(input("OWN EMAIL \n"))
merapswd = str(input("OWN PASSWORD \n"))

yagmail.register(meraemail, merapswd)

print("")
print("NOW MAIN TASK")
print("")

print("loggedin")
with yagmail.SMTP(meraemail) as yag:
    with open("mailinglist.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for email, ousername, opassword in reader:
            contents = [
                f"HOW YOU DOING ? {email}",
                "YOUR ORACLE ID AND PASSWORD HAS BEEN CREATED",
                "",
                f"Your USERNAME is :  {ousername}",
                f"Here is your PASSWORD:  {opassword}",
                "",

                "To get started using the Oracle Academy Member Hub:",
                "1. Go to academy.oracle.com.",
                "2. Locate and select Sign In in the top right corner and click Sign in to Student Hub.",
                "3. Enter your username and password.",
                "Upon first access, you will be prompted to change your password, ",
                " set your preferred language and time zone. ",
                "As a gentle reminder, students will work directly  with their instructor  ",
                "on any technical questions associated with their accounts. ",
                "",
                "",
                "REGARDS,",
                "VINAY PANCHAL",
                "http://vinaypanchal.com",

            ]
            yag.send(email, 'ORACLE ACCOUNT CREDENTIALS', contents)
            print("SENT  "+email)
            print("ID   "+ousername)
            print("password  "+opassword)
            print("")
print("")
print("TASK SUCCESSFULLY COMPLETED")
