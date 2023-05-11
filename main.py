#Prince Prajapati

#Check the IP Address of the current location
#Importing package namked Socket to know IP.
import socket as s
hostn = s.gethostname()
IP = s.gethostbyname(hostn)
print("IP ADDRESS IS"+ IP)


#Generate random password in Python!!
#import packages named Random and string
import random
import string
LETTERS =  string.ascii_letters
NUMS = '0123456789'
SPE = '-+*%&$!_'
SYMBOLS = LETTERS + NUMS + SPE
len = int(input("ENTER PASS.LENGTH:"))
password = "".join(random.sample(SYMBOLS,len))
print(password)

# #QR Code generator
# #PIL = Pillow package
# import os
# import pyqrcode
# from PIL import Image
#
# class QR_Gen(object):
#     def __init__(self, text):
#         self.qr_image = self.qr_generator(text)
#
#     @staticmethod
#     def qr_generator(text):
#         qr_code = pyqrcode.create(text)
#         file_name = "QR Code Result"
#         save_path = os.path.join(os.path.expanduser('~'), 'Desktop')
#         name = f"{save_path}{file_name}.png"
#         qr_code.png(name, scale=10)
#         image = Image.open(name)
#         image = image.resize((400,400),Image.ANTIALIAS)
#         image.show()
#
# if __name__=="__main__":
#    QR_Gen(input("[QR] https://www.anonymous.education/p/miscellaneous-py-codes.html:"))


#Check weather updates
#importing package named requests
import requests
from bs4 import BeautifulSoup
search="Weather in Waterloo"
url = f"https://www.google.com/search?&q={search}"
r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
update = s.find("div",class_="BNeawe").text
print(update)


#Fibonacci Sequence
terms = int(input("Enter the Number:"))
a = 0
b = 1
count = 0
#Applies If, else statement
if (terms<=0):
   print("Please enter a valid integer")
elif (terms==1):
   print("Fibonacci Sequence  upto", terms, ":")
   print(a)

else:
   print("Fibonacci sequence:")
   while (count < terms):
      print(a, end = ' ')
      c = a+b
      #updating values
      a = b
      b = c
      count +=1