'''
Created on 2022-01-20

@author: Ananthakrishnan.G

source:
    https://builtin.com/data-science/python-ocr
    https://stackoverflow.com/questions/44619077/pytesseract-ocr-multiple-config-options

'''

from PIL import Image
from pytesseract import *
import os
import cv2

folder=os.listdir("/home/ananthu/folder_name/")

for files in folder:
    loc="/home/ananthu/tact/folder-name/"+files
    img = Image.open(loc)
    # box = (250, 250, 750, 750)
    # img2 = img.crop(box)
    text = pytesseract.image_to_string(img,config='--psm 6')
    # print(text)
    
    f=open("/home/ananthu/tact/folder-name/file-name.txt","a")
    f.write(text)
    f.close()
    