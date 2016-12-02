'''
input: input integer.
output: True or False
'''
def PerfectSquare(x):
    n = 0                                                                             # 1              
    if x >= 0:                                                                     
        while n*n < x: #will keep multipling n by itsself until the number is reached                               
            n = n +1#this allows the loop to end as eventually n*n will more or equal to x                            
            print(n,'*',n,'=',n*n)                                    
        if n * n != x:                          
            return False                              
        else:                                   
            return True              
    else:
         print("End")    
print(PerfectSquare(35))        

#line by line 
#big) = 0(log(n))
  #1+1+1+1++n+n+n+1+1+1+++++

