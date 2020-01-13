#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:27:43 2020

@author: oscardolloway
"""

def Bruteforce(list1,list2,target):
    
    
    for i in range(len(list1)):
        element = list1[i]
        print(element)
        j=i#position
        print(list1[j-1])
        while j > 0 and list1[j-1] > element:
            list1[j] = list1[j-1]
            j = j-1
        list1[j] = element
    print( list1)
    
    
        
        #print(target)
        #if check == target:
        #    break
        #    print('target found')
        #else:
        #    selected = list1[count]
        #    count = count+1
        #    print(count)
        
        
        
#Bruteforce([1,8,9,7],[9,10,2,1],11)
        
def find_sum(array_test):
    total = 0
    for i in array_test:
        total+= i
        print( total)

#array_test = [1,4,3,2,10]
#find_sum(array_test)


#while list is not empty:
#        check
#        then pop
lista  = "aaabbggg"

def split(word): 
    return [char for char in word]

dictest = {i: 0for i in lista}
#while lista != 0:
lista = (split(lista))

index = 0

def check1 (lista, index):
    Target = 5
    if index > len(lista):
        
        print(" False")
    elif Target == index:
        print("True")
    else:
         print (lista[index])
         check1 (lista,index+1)
            
    
#check1([1,2,9,4,5,6],0)

    
#count = 0
#for i in (lista):
#    print(i)
#    if i == 'a':
#        count = count+1
#        print(count)
    #if lista[i] is lista[i-1]:
    #   print('he')
    

letter = 'a'
myString = 'aarrrdvark'
myList = []
count = sum(i == letter for i in myString)
res = []
for i in lista:
    if i not in res:
        res.append(i)
        


def Sequence1(integers):    
    longestSeq = []
    currentSeq = []
    count = []
    i = 0
    for i in range( len(integers) ) :
        #sequence continues to the length of sequence
        print(integers[i])
        if i < len(integers)-1 and integers[i] == integers[i+1]: # checks if list is in acesending order.
            #integers.pop(0)
            #append the current subsequence to list currentSeq
            print(len(integers)-1)
            currentSeq.append(integers[i])
            print('current seqeuence = ',currentSeq)
        else:
            currentSeq.append(integers[i])# gets last integer and stores it with currentSeq(was an error originally
            print('\subsequence ended', currentSeq)
            #checks the length of currentSeq with LongestSeq so we know which is the longest at the moment
            if len(currentSeq) > len(longestSeq):
                print('\n')#looks messy without
                #replaces the longest with current if its longer.
                longestSeq = currentSeq
            #reset current sequence tracker
            currentSeq = []
    print()
    print ('longest sequence = ', longestSeq)
#we store the subsequence we're looking at as currentSeq,
#we then check the length of current with longest if current is longer it replaces the longest.
#we then reset currentSeq as empty and loop back round and do the same with the next subsequence
Sequence1(["a","a","b","b","b","c","b"])