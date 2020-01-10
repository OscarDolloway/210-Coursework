'''
input: string
output: Reversed String

Reverse Function - reverses the string using a forloop.
the forloop knows to stop because as the list reverses i also delete it
'''

s = "aaabbccc"


#s = String.split(" ") #stops the letters reversing instead of the word
newlist = []
for i in range(len(s)-1,0,-1):#start at the end of the list, stop at 0 and go down the list 1
    print(s[i],i)
    
    if string[i] is string[i+1]:
        print('same')
    
    #while i < len(s):
    #    continue
    #    print("yes")
        
    newlist.append(s[i])

    #    print(s[i])
        #if string[i] > len(s):
        #    break
    #newlist[a] = (s)#appends the reverse element into the reverse array
    #del s[-1]
print(newlist)
# =============================================================================
#Reverse1(s)
# =============================================================================

#print (reversestring)
#brute force search to reach a target number
#2 lists
#pick 1 element from 1 list and put it into empty array
#compare the chosen element with the all the oppersite list elements until
# reachs goal if not move onto second element
#improvements could be -chosen element from goal number and then look for that specific number
#list1 = [1,5,8,3,7,9]
#list2 = [1,5,10,3,6,9]