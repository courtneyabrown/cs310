#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:11:04 2020

@author: courtneybrown
"""

def next_states(s):
    list = []
    if s.endswith("I"):
        new = s + "U"
        list.append(new)
    if s.startswith("M"):
        new = s + s[1:]
        list.append(new)
    if "III" in s:
        for i in range(len(s)):
            x = s.find("III", i, i + 3)
            if x != -1:
                new = s[:x] + "U" + s[(x + 3):]
                list.append(new)
    if "UU" in s:
        new = s.replace("UU", "")
        list.append(new)
    return list