from __future__ import division, print_function, unicode_literals

import os
import sys
import random
from PIL import Image
import argparse
import logging
import wget
import numpy as np
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import cv2
from math import log
from tqdm import tqdm
import show


def ArnoldCatDecryption(imageName, key):
    img = cv2.imread(imageName)
    
    for i in range(0,key):
        img = ArnoldCatTransformdec(img)
    img1 = cv2.imread("secret.png")
    h,w,_= img1.shape
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

def ArnoldCatTransformdec(img):

    h,w,_=img.shape
    decrypted_image = np.zeros([h,w,3])
    if h!=w:
        raise exception ("Expected a square image")
    for x in range(0,h):
        for y in range(0,h):
            decrypted_image[x][y]=img[(x-y)%h][((2*y)-x)%h]
    return decrypted_image
 
def decrypt_image():
    ArnoldCatDecryption("secret_ArnoldcatEnc.png", 5)
    ArnoldCatDecryption("ciphered_ArnoldcatEnc.png", 7)
    show.decrypted_image()
    img=Image.open('original.png')
    img.show()

decrypt_image()

