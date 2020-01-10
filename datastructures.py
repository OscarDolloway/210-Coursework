#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:27:51 2020

@author: oscardolloway
"""

string = ["a","a","a","b","b","b","c","c","c","c"]

#i = -1
reversed = []
def reverse (string):
    for i in range(len(string)-1):
        print(i)
        for j in range(i):
            print(j)
            if string[i] == string[i+1]:
                string[i+1] = string[i]
            #print(string[i])
        
            #print(string)

#reverse(["a","a","a","b","b","b","c","c","c","c"])
    #for a in i:
     #   print(a)
    #if i == 'a':
    #    print('Hello')
    
    

def bubblesort(List):
    for i in range(len(List)-1,0,-1):
        for j in range(i):
            if List[j] == List[j+1]:
                temp = List[j]
                print(temp)
                List[j] = List[j+1]
                List[j+1] = temp
                print(temp)
            print(List)
    return List
print(bubblesort(["a","a","b","b","b","b"]))
#for loop to length of string
    #if element 1 == to element 2
        #delete element 2
    #else continue through list
    
    
    
    