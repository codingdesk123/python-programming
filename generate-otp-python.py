import os
import random
import string

#loop to Generate 7 Digit OTP
OTP = ''.join([random.choice( string.ascii_uppercase + string.ascii_lowercase + string.digits) for n in range(6)])

#final OTP will be stored in this variable "your_otp"
your_otp = "'"+OTP+"' is your OTP"

#Printing the OTP
print(your_otp)

#Code for Correct and Incorrect Entries
for i in range(1,4):
    a = input("Enter Your OTP: ")
    if a == OTP:
        #If entered OTP is Correct it prints verified and break
        print("Verified Successfully\n ")
        break
    else:
        #executes when entered OTP is Wrong
        print("Please Check Your OTP")
        attempts = 4 - (i+1)
        if(attempts == 1):
            print("***",attempts,"attempt is remaining *** \n")
        elif(attempts > 0):
            print("***", attempts, "attempts are remaining *** \n")
        else:
            print("\n Sorry, You have reached too many attempts, Try after Sometime")




            
