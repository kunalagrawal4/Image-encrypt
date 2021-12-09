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


def decrypted_image():
    infile1 = Image.open(os.path.join(r'ciphered_ArnoldcatDec.png'))
    infile2 = Image.open(os.path.join(r'secret_ArnoldcatDec.png'))
    infile2 = infile2.convert("1")
    infile1 = infile1.convert("1")
    outfile = Image.new('1', infile1.size, color=255)
    for x in range(infile1.size[0]):
        for y in range(infile2.size[1]):
            outfile.putpixel((x, y), max(infile2.getpixel((x, y)), infile1.getpixel((x, y))))

    outfile.save('original.png')


def decrypt_image(f1,f2):
    f1 = Image.open(f1)
    f2= Image.open(f2)
    f1.save("secret_arnoldenc.png")
    f2.save("ciphered_arnoldenc.png")
    ArnoldCatDecryption("secret_arnoldenc.png", 3)
    ArnoldCatDecryption("ciphered_arnoldenc.png", 22)
    decrypted_image()
    if os.path.exists("secret_arnoldenc.png"):
        os.remove("secret_arnoldenc.png")
    if os.path.exists("ciphered_arnoldenc.png"):
        os.remove("ciphered_arnoldenc.png")
