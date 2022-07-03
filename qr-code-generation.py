from verify_email import *
# import verify_email
import validate_email
import os
import math
import random
import smtplib
import pyqrcode
from pyqrcode import QRCode
from tkinter import *
from tkinter import messagebox


def qrgen():


    ws = Tk()
    ws.title("Suguna's Project")
    ws.config(bg='skyblue')

    def generate_QR():
        if len(user_input.get()) != 0:
            global qr, img
            qr = pyqrcode.create(user_input.get())
            img = BitmapImage(data=qr.xbm(scale=8))
        else:
            messagebox.showwarning('warning', 'All Fields are Required!')
        try:
            display_code()
        except:
            pass

    def display_code():
        img_lbl.config(image=img)
        output.config(text="QR code of " + user_input.get())

    user_input = StringVar()
    entry = Entry(
        ws,
        textvariable=user_input
    )
    entry.pack(padx=30)

    button = Button(
        ws,
        text="generate_QR",
        width=15,
        command=generate_QR
    )
    button.pack(pady=30)

    img_lbl = Label(
        ws,
        bg='white')
    img_lbl.pack()
    output = Label(
        ws,
        text="",
        bg='yellow'
    )
    output.pack()

    ws.mainloop()
Name = input("Enter your Name: ")
m = input("Enter your email:")
def qr():
    # String which represent the QR code
    p = "https://",input("Enter link: ")

    # Generate QR code
    url = pyqrcode.create(p)
    img = BitmapImage(data=url.xbm(scale=8))
    print(img)
    # print(url.terminal(quiet_zone=1))
    #Create and save the png file naming "qrname.png"
    #url.svg("mywebsite.svg", scale=8)
def wrong_otp():
    o = input("Enter Your OTP: ")
    if o == OTP:
        print("Verified")
        qrgen()
    else:
        print("Please Check your OTP again")
digits="0a1b2c3d4e5f6g7h8i9"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg = otp
print(msg)
your_otp = input("Enter Your OTP: ")
if your_otp == OTP:
    print("Verified")
    qrgen()
else:
    print("Please Check your OTP again")
    wrong_otp()
