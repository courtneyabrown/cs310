#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:13:42 2020

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

def extendPath(p):
    result = []
    temp = []
    newpath = next_states(p[-1])
    for i in newpath:
        temp = []
        for j in p:
            temp.append(j)
        temp.append(i)
        result.append(temp)
    return result

def breadthFirstSearch(goalString):
    agenda = [["MI"]]
    count = 0
    maxAgenda = 0
    while (len(agenda) != 0):
        if (count < 1000):
            currentPath = agenda.pop(0);
            if (goalString == currentPath[-1]):
                print("The length of the path is:", len(currentPath))
                print("The number of times that extendPath(p) was called is:", count)
                print("The maximum size of the agenda is:", maxAgenda)
                print("The value of currentPath is:", currentPath)
                return "Found it!"
            nextVar = extendPath(currentPath)
            agenda = agenda + nextVar
            count = count + 1
            if (len(agenda) > maxAgenda):
                maxAgenda = len(agenda)
        else:
            return []
        
def depthlimited_dfs(goalString, limit):
    agenda = [["MI"]]
    count = 0
    maxAgenda = 0
    while (len(agenda) > 0):
        if (maxAgenda < len(agenda)):
            maxAgenda = len(agenda)
        currentPath = agenda.pop(0);
        if (goalString == currentPath[-1]):
            print("The length of the path is:", len(currentPath))
            print("The number of times that extendPath(p) was called is:", count)
            print("The maximum size of the agenda is:", maxAgenda)
            print("The value of currentPath is:", currentPath)
            return "Found it!"
        elif (len(currentPath) < limit):
            nextVar = extendPath(currentPath)
            agenda = nextVar + agenda
            count = count + 1
    return []

def dfs_iter(goalString):
    limit = 2
    while (not depthlimited_dfs(goalString, limit)):
        limit = limit + 1