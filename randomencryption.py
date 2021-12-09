from PIL import Image
import numpy as np
import os
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import cv2
import random
from math import log
from tqdm import tqdm
import wget

# https://drive.google.com/uc?id=121nAa2VP6d8NedUWqzuoncqfKFm_ttWJ
# https://i.picsum.photos/id/800/200/300.jpg?hmac=p2lPeodOve_jNKshk2YAKVhKm4UUIJhfUe_Tt4FdnTA
# https://i.picsum.photos/id/778/300/200.jpg?hmac=lULcx7uCqA-UiRLH2Xw_eo6gLrLR2AMlrQ1exS7HKd4
# https://picsum.photos/200/300

url = input("paste link for the file: ")
filename = wget.download(url,'hello.jpg')

    
def ArnoldCatTransform(img, num):
    
    h,w,_=img.shape
    n=max(h,w)
    img_arnold = np.zeros([n,n,3])
    padding = ((0,n-h),(0,n-w),(0,0))
    img=np.pad(img,padding,'constant',constant_values=255)
    for x in range(0,n):
        for y in range(0, n):
            img_arnold[x][y] = img[(x+(3*y))%n][((7*y)+(2*x))%n]  
            # value for p and q =2 and 3
    return img_arnold 

    
def ArnoldCatTransformdec(img):

    h,w,_=img.shape
    decrypted_image = np.zeros([h,w,3])
    if h!=w:
        raise exception ("Expected a square image")
    for x in range(0,h):
        for y in range(0,h):
            decrypted_image[x][y]=img[((7*x)+((-3)*y))%h][((y)-(2*x))%h]
    return decrypted_image
    
def ArnoldCatEncryption(imageName, key):
    img = cv2.imread(imageName)
    for i in range (0,key):
        img = ArnoldCatTransform(img, i)
    cv2.imwrite(imageName.split('.')[0] + "_ArnoldcatEnc.png", img)
    return img

	

def ArnoldCatDecryption(imageName, key, original):
    img = cv2.imread(imageName)
    original = cv2.imread(original)
    for i in range(0,key):
        img = ArnoldCatTransformdec(img)
    h,w,_= original.shape
    if h>w:
        z=1
        n=h
    else:
        z=0
        n=w
    w=min(h,w)
    img = np.delete(img,slice(w,n+1),z)
    cv2.imwrite(imageName.split('_')[0] + "_ArnoldcatDec.png",img)
    return img


image = "hello"
ext = ".jpg"
key = 20


img = cv2.imread(image + ext)
im = Image.open(r'./hello.jpg') 


ArnoldCatEncryptionIm = ArnoldCatEncryption(image + ext, key)
enc = Image.open(r'./hello_ArnoldcatEnc.png') 


ArnoldCatDecryptionIm = ArnoldCatDecryption(image + "_ArnoldcatEnc.png", key, image + ext)
dec = Image.open(r'./hello_ArnoldcatDec.png') 

im.show() 
enc.show()
dec.show()



