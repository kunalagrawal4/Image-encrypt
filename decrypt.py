import os
from PIL import Image
import sys
import os
import sys
import random
from PIL import Image
import argparse
import logging

infile1 = Image.open(os.path.join(r'ciphered_ArnoldcatDec.png'))
infile2 = Image.open(os.path.join(r'secret_ArnoldcatDec.png'))

outfile = Image.new('1', infile1.size, color=0)
for x in range(infile1.size[0]):
    for y in range(infile2.size[1]):
        outfile.putpixel((x, y), min(infile2.getpixel((x, y)), infile1.getpixel((x, y))))

outfile.save('original.png')