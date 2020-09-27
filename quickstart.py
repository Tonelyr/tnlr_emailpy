import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com" # Gmail SMTP server
sender_email = open(r"your_email.txt", "r")
receiver_email = open(r"receiver_email.txt", "r")
password = open(r"your_password.txt", "r")
message = """\
Subject: __

Insert Text

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
