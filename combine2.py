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


def load_image(name):
    return Image.open(name)

def prepare_message_image(image, size):
    if size != image.size:
        image = image.resize(size)
    return image.convert("1")

def generate_secret(size):
    width, height = size
    new_secret_image = Image.new(mode = "1", size = (width * 2, height * 2))
    old_width, old_height = (-1, -1)
    for x in range(0, 2 * width, 2):
        for y in range(0, 2 * height, 2):
            if x < old_width and y < old_height:
                color = secret_image.getpixel((x, y))
            else:
                color = random.getrandbits(1)
            new_secret_image.putpixel((x,  y),   1-color)
            new_secret_image.putpixel((x+1,y),   color)
            new_secret_image.putpixel((x,  y+1), 1-color)
            new_secret_image.putpixel((x+1,y+1), color)
    
    
    return new_secret_image

def generate_ciphered_image(secret_image, prepared_image):
    width, height = prepared_image.size
    ciphered_image = Image.new(mode = "1", size = (width * 2, height * 2))
    for x in range(0, width*2, 2):
        for y in range(0, height*2, 2):
            secret = secret_image.getpixel((x,y))
            message = prepared_image.getpixel((x/2,y/2))
            if (message > 0 and secret > 0) or (message == 0 and secret == 0):
                color = 0
            else:
                color = 1
            ciphered_image.putpixel((x,  y),   color)
            ciphered_image.putpixel((x+1,y),   1-color)
            ciphered_image.putpixel((x,  y+1), color)
            ciphered_image.putpixel((x+1,y+1), 1-color)
    
    return ciphered_image

def ArnoldCatTransform(img, num):
    h,w,_=img.shape
    n=max(h,w)
    img_arnold = np.zeros([n,n,3])
    padding = ((0,n-h),(0,n-w),(0,0))
    img=np.pad(img,padding,'constant',constant_values=4)
    for x in range(0,n):
        for y in range(0, n):
            img_arnold[x][y] = img[(2*x+y)%n][(y+x)%n]  
    return img_arnold 

def ArnoldCatEncryption(imageName, key):
    img = cv2.imread(imageName)
    for i in range (0,key):
        img = ArnoldCatTransform(img, i)
    cv2.imwrite(imageName.split('.')[0] + "_ArnoldcatEnc.png", img)
    return img

	

def encrypt(filename):
    message_image = Image.open(filename)
    size = message_image.size
    secret_image = generate_secret(size)
    prepared_image = prepare_message_image(message_image,size)
    ciphered_image = generate_ciphered_image(secret_image, prepared_image)
    ciphered_image.save("ciphered.png")
    secret_image.save("secret.png")
    prepared_image.save("prepared_message.png")
    ArnoldCatEncryption("secret.png", 5)
    ArnoldCatEncryption("ciphered.png", 7)
