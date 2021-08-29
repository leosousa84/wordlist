#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unicodedata
import sys

def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)

arquivo = sys.argv[1]

palavra = open(arquivo, 'r')
with open(arquivo, mode='r') as f:
    for i in f:
        s = strip_accents(i)
        linew = open('wl-novo', mode='a+', encoding='ascii')
        linew.writelines(s)
        print(s)
