def Sequence1(integers):    
    longestSeq = []
    currentSeq = []
    i = 0
    for i in range( len(integers) ) :
        #sequence continues to the length of sequence
        if i < len(integers)-1 and integers[i] <= integers[i+1]: # checks if list is in acesending order.
            #append the current subsequence to list currentSeq
            currentSeq.append(integers[i])
            print('current seqeuence = ',currentSeq)
        else:
            currentSeq.append(integers[i])# gets last integer and stores it with currentSeq(was an error originally
            print('\subsequence ended', currentSeq)
            #checks the length of currentSeq with LongestSeq so we know which is the longest at the moment
            if len(currentSeq) > len(longestSeq):
                print('\n')#looks messy without
                #replaces the longest with current if its longer.
                longestSeq = currentSeq
            #reset current sequence tracker
            currentSeq = []
    print()
    print ('longest sequence = ', longestSeq)
#we store the subsequence we're looking at as currentSeq,
#we then check the length of current with longest if current is longer it replaces the longest.
#we then reset currentSeq as empty and loop back round and do the same with the next subsequence
Sequence1([1,2,3,4,5,1,2,4,5,6,7,1,2,3])