import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com" # Gmail SMTP server
sender_email = "EMAIL@gmail.com"
receiver_email = "name@domain.com"
password = "PWD"
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
