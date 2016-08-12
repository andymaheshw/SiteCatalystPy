# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 07:15:09 2016

@author: anirudhmaheshwari
"""

def test_setup():
    f = open('creds.txt', 'r')
    print(f.readline())
    
test_setup()