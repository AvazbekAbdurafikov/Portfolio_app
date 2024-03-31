import smtplib, ssl

host = "smtp.gmail.com"
port = 465
username = "nursultonavazbek@gmail.com"

password = "frpdrmfbareottxm"

reciver = 'nursultonavazbek@gmail.com'
contex = ssl.create_default_context()

message = """
Hi
How are you?
Bye!
"""
with smtplib.SMTP_SSL(host=host, port=port, context=contex) as server:
    server.login(username, password)
    server.sendmail(username, reciver, message)

