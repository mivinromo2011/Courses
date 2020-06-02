#!/bin/python3
import smtplib

usr = "mivintemp@gmail.com"
password = "P#mjfSr(rk5]BiFCjMG7,(*kAZY_KH&z"
#print (password)
sender = 'mivintemp@gmail.com'
receivers = ['mithun.rosinth@gmail.com'] 

message = """From: From Person <you@domain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test
This is a test e-mail message.
"""
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(usr,password)
server.sendmail(sender, receivers, message)
