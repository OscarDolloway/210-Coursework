'''
input: input from user x, any positive number
output: number of Trailing zeros in x
'''
def count1 ():
    zeros = 0           #1
    x = input()         #1
    x = int(x)          #1
    for i in range (2,x+1): #n
        #print(i)
        if x > 0:
            if i % 5 == 0:       #1
                zeros +=1
                i = i/5
        else:
            ("False")
    print(zeros)
    return zeros

#count1()
#factorial number = a number multiplied by its decending number i.e 5*4*3*2*1 
#trailing zero = 5*4*3*2*1 = 120 therefore 1 trailing zero,
# % always gives you last element
#zeros += 1 adds the zero count so we get the correct total at the end
#we modulus by 5 so we can see how many times five fits into x, if 5 fits into x there are 0 spare numbers
#1+1+1+1+1+1+1+n
#7n
#n
#o(n)

def Trailing_Zeroes(x):
    fives = 0
    for i in range(2, x+1):
        print(i)
        while i > 0:
            if i % 5 == 0:
                print(i % 5)
                fives += 1
                i = i/5
            else:
                break
    print(fives)
    return fives


#Trailing_Zeroes(40)

def test():
    x = 10
    m = x % 2
    z = x % 5
    y = x % 10
    print("z=",z,"y=",y,"m=",m)
#test()

'''
Function count - Counts the number of trailing zeros

This will start out checking how many 5s are in x so x/5, then 25, then 125,
if the number is a whole number, it goes towards the trailing zeros,
if not it will stop display the number of zeros

zeros += x // i#count, the number is determined by how many times x goes into i
output:
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
    

print(count(100))
'''i *= 5: will start out checking how many 5s are in x so x/5, then 25, then 125,
if the number is a whole number, it goes towards the trailing zeros, if not it will stop display the number of zeros'''
#



def fac():
    num = 100
    factorial = 1
    if num < 0:
        
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)
        
    
#fac()

#alist = [1,2,3,4,5,6]

#alist.pop()
#alist.append(5)
#print(alist)


