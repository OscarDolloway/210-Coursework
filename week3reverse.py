'''
input: string
output: Reversed String

Reverse Function - reverses the string using a forloop.
the forloop knows to stop because as the list reverses i also delete it
'''

s = "#Diana for president!"
def Reverse1(String):

    s = String.split(" ") #stops the letters reversing instead of the word
    reverse = [] 
    i = 0
    for i in range(len(s)): 
        reverse.append (s[-1])#appends the reverse element into the reverse array
        del s[-1]
    return reverse
print(Reverse1(s))

