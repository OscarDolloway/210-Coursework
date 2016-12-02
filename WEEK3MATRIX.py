matrix = [[8,10,3,4,5],[1,2,3,4,5]]
matrix1 = [[1,10,70,10,5],[9,2,4,4,5]]
results = [[0,0,0,0,0],[0,0,0,0,0]]
    
    #i = (len(matrix))#rows
    #j = (matrix [0])#columns

def add():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            results[i][j] = matrix[i][j]+matrix1[i][j]
    for r in results:
        print(r)

def sub():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            results[i][j] = matrix[i][j]-matrix1[i][j]
    for r in results:
        print(r)

def multiple():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            results[i][j] = matrix[i][j]*matrix1[i][j]
    for r in results:
        print(r)
   
def calc():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            results[i][j] = matrix[i][j]*matrix1[i][j]-2*(matrix[i][j]+matrix1[i][j])#1
    for r in results:
        print(r)
#forloop(nxnxn = O(N^3)


print(" Addition")
add()
print("\n","Subtraction")
sub()
print("\n","Multiplication")
multiple()
print("\n","A= B*C-2*(b+C)")
calc()
#def add(matrix,matrix1):
    #i = (len(matrix))
    #j = (matrix [0])
    
    #print(i)
    #print(j)
#add()
def sub():
    pass


def multiple():
    pass


#n = matrix[i]+[j]

#print(n)
#print(matrix1[0:1])#matrix 1


#for i in matrix1:
    #print ([i])

#matrix 2



#matrix = [[0] * ncols for i in range(nrows)]
#matrix[2][0] = 5 
#matrix[0][2] = 5 

#print(matrix)



#print(matrix[0][2]+matrix[0][2])

ncols = 4
nrows = 4
matrix2 = []
for i in range(nrows):
    #print(i)
    matrix2.append([0] * ncols)


matrix2[1][0] = 1
matrix2[1][1] = 5 
matrix2[1][2] = 8
matrix2[1][3] = 9

matrix2[0][0] = 10
matrix2[0][1] = 6 
matrix2[0][2] = 3
matrix2[0][3] = 8

matrix2[2][0] = 10
matrix2[2][1] = 6 
matrix2[2][2] = 3
matrix2[2][3] = 8

matrix2[3][0] = 11
matrix2[3][1] = 6 
matrix2[3][2] = 3
matrix2[3][3] = 8

#print(matrix2[0]+matrix2[1])


