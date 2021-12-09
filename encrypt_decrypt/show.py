import os
from PIL import Image
import sys
import os
import sys
import random
import argparse
import logging

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