

'''
Function count - Counts the number of trailing zeros

This will start out checking how many 5s are in x so x/5, then 25, then 125,
if the number is a whole number, it goes towards the trailing zeros,
if not it will stop display the number of zeros
i *= 5: will start out checking how many 5s are in x so x/5, then 25, then 125,
if the number is a whole number, it goes towards the trailing zeros,
if not it will stop display the number of zeros
input: any number above 1
output: zeros
'''
def count(x):
    i = 5#this is 5 so we can check x/5 to begin with
    zeros = 0 
    while x / i >= 1:#while 30 / 5 is greater than or == 1 if not return zero and loop ends!!
        print("i =",i)
        print("trailing zeroes counted:",x//i)
        zeros += x // i#count, the number is determined by how many times x goes into i 
        i *= 5
    print("Total zeros in",x,":")
    return zeros
    
#O log(n)
#print(count(100))


