# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 18:51:44 2024

@author: hp
"""

f1 = open('1.png', 'rb')
f2 = open('1_reverse.png', 'wb')
f2.write(f1.read()[::-1])
f2.close()
f1.close()
