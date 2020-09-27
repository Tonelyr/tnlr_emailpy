import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "hahahfivebotgobrrrrrrrrrrrrr@gmail.com"
receiver_email = "phelpgae@nerdoron.me"
#receiver_email = "johncena694204206969@gmail.com"
password = "haha69funni"
message = """\
Subject: Hi there

Phelps gae Phelps gae

Yes FiveBot cool better than mee6 quote this because Tonelyr is very good man

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)