
'''
BinarySearch Function - This function determines whether a value is between low and high
it does this by making the value the midpoint.

input: alist, low and high.
output:True or False
'''

def binarySearch(alist,low, high):
    first = 0                               
    last = len(alist)%10                                               
    found = False                           
    while first < last and not found:       
        midpoint = (first + last)//2
        print(midpoint)
        if alist[midpoint] < high and alist[midpoint] > low:  #thecheck    
            found = True
        else:
            if alist[midpoint] > high:
                last = midpoint-1
            else:
                first = midpoint+1
    return found
print (binarySearch([1,2,3,4,5,6,7,8,9],1,2))

#first = 0, first index within the list
#last = len(alist)%10, always return last index
#found = False, we can return True or False by declaring this variable
#midpoint = (first+last)//2 will find the element at centre of the list
#if midpoint <= high and midpoint >= low will find out if midpoint is between high and low
#then will return TRUE and end loop
#if the previous statement isnt true it will then half the list by switching the first and last values,
#if the midpoint is more than high the midpoint will become 'last = midpoint-1',
#this will then go back through loop with the last changed.

