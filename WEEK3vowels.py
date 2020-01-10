
def vowels(word,count):  
    
    #novowels = word
    vowels = ['aeiou']#contains all vowels
    vowels.replace(""," ")
    for x in word:#x is a vowel we check if the word contains the vowel
        if x in vowels:
            print(x)
            word = word.replace(x,"") # replaces x(vowel) with an empty space
            count = count+1
    print(count)
    print(word)
vowels('beautiful',0)
#x = each letter of word
#we define a novowels as strings have to be replaced




