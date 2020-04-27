#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:26:22 2020

@author: courtneybrown
"""

def collatz(n):
    i = 1;
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            i = i + 1
        else:
            n = n * 3 + 1
            i = i + 1
    return i

def biggest_seq(end):
    n = 1
    biggest = 1
    while n <= end:
        if collatz(n) > biggest:
            biggest = collatz(n)
            size = n
        n = n + 1
    print ("The biggest collatz sequence is", size, "with a length of", biggest)