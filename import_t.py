# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 14:35:00 2018

@author: win
"""

def make_album(singer,zjn,singnum):
    dict1 = {}
    dict1['singer'] = singer
    dict1['zjn'] = zjn
    if singnum:
        dict1['singnum']=singnum
    return dict1