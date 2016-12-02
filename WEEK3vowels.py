def vowels(word):  

    #novowels = word
    vowels = ['a','e','i','o','u']#contains all vowels
    for x in word:#x is a vowel we check if the word contains the vowel
        if x in vowels:
            word = word.replace(x,"") # replaces x(vowel) with an empty space
    print(word)
vowels('beautiful')
#x = each letter of word
#we define a novowels as strings have to be replaced




