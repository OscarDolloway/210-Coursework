import random
import random
'''
Function Shuffle- shuffles the arrays around by the length of the list
creates two random positions within the list and switches them around
'''
def shuffle( Integers ): 
    print (Integers)
    for i in range(len(Integers)): # len(Integers) so it shuffles the length of the list
        x = random.randint (0,len (Integers)-1)#random location within list
        y = random.randint (0,len (Integers)-1)
        Integers[x], Integers[y] = Integers[y], Integers[x] #flips elements around
    return Integers   
print(shuffle([5,6,7,10,11,12]))

#O = o(n)


