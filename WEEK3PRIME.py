



'''
Prime function will determine wether a number is prime,

It does this by checking if a number other than itself and 1 is divisable
if so it isnt a prime


'''

## first statement: rules of prime, if the number is above 2 and even its not a prime
#x is the number were using
#x%2checks for even numbers
#x%i will check if any number goes into x,
#i increases by one as we have a range so every number 
x = 67



'''
Prime function will determine wether a number is prime,

It does this by checking if a number other than itself and 1 is divisable
if so it isnt a prime


'''
#recursive
#if the number is above 2 and even its not a prime
def Prime(i,Number):
    #print(a, Number)
    if Number <= 1:#ends if number is 1 or less
        return 
    else:
        if i >= Number: # 
            print("Prime",Number)
        else:
            if Number == 2: ## if number is two it is a prime number the only prime even number
                print(Number)
            elif (Number % i) == 0:# if there is no remainders it means the number goes into it making it not a prime number
                print( False)

            else:
                return Prime(i+1,Number)#i we recursive do i = i+1 untill we reach the number

    return False

Prime(2,14)








#ui = input("please Enter string: ")

#Target = input("enter substring")

haystack = input()
needle = input()

cnt = 0
for ii in range(0, len(haystack) - len(needle) + 1):
    if haystack[ii:ii + len(needle)] == needle:
        print(haystack[ii:])
        cnt = cnt + 1

print (cnt)










