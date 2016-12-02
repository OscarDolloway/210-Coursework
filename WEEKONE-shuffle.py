import random
'''
Function: 
input: random integer between 1 and 19
output: array of 10 random integers
'''
##function shuffle: ten random integers are appended to an empty array
## while loop finishes when count turns to 10
def shuffle():
    aList = []                          #1
    x = False                           #1
    count = 0                           #1
    while x == False:                   #
        aList.append ( random.randint(0,20) )       #1
        if aList.append:                            #
            count = count+1                         #
            #print (count)
            if count == 10:                         #
                x = True                            #
    print(aList)                                    #1
#shuffle()                                           #

#bigO = O (n)

'''
Function Shuffle- shuffles the arrays around by the length of the list
creates two random positions within the list and switches them around
'''
def shuffle( Integers ): 
    print (Integers)
    for i in range(len(Integers)): # len(lis) so it shuffles the length of the list
        x = random.randint (0,len (Integers)-1)#random location within list
        y = random.randint (0,len (Integers)-1)
        Integers[x], Integers[y] = Integers[y], Integers[x] #flips elements around
    return Integers
    
    
print(shuffle([5,6,7,10,11,12]))

#ON = o(n)

