class BinTreeNode():
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
 
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print(tree.value)
    if(tree.right!=None):
        in_order(tree.right)

#call the root
#check left hand side, change root to left
#keeps changing till last value with no left hand side is printed
#check right hand side, change root to right
#same again

'''
Function in_order1 uses a stack to display an array of nodes in order
tree = 6,10,5,2,3,4,11
-i have created thestack[] and a visited array called alreadybeen[]
-i defined the current node as 'current node = thestack[-1] this gives the the only value in the stack
-The whileloop in this function continues till the stack is empty,
we empty it at the end of the loop by popping(thestack.pop())

-The first IF statement checks if there are values to the left(currentnode.left) of the current node.
if so we append it to the stack.
This continues until we have no values to the left then we move onto the right.
-The Elif statement does the same for the right hand side(currentnode.right)
however we create another condition inside to stop repeating nodes being printed.
'if currentnode not in alreadybeen:' this ensures that when the program goes back up the tree the same values are not printed or appended
we then print values to get the left hand values.
-else statement we print the rest of the nodes so this will give us the right hand values
then we pop to empty the stack so the the loop ends.
'''
def in_order1(tree):
    thestack = [tree]
    alreadybeen = []
    #print(alreadybeen)
    while len(thestack) > 0:
        currentnode = thestack[-1]
        
        if currentnode.left and currentnode.left not in alreadybeen:#checks lefthand side
            #print(currentnode.value)
            thestack.append(currentnode.left)
            
        elif currentnode.right and currentnode.right not in alreadybeen:#checks right hand side
           if currentnode not in alreadybeen:#stops repeating values being appended
                alreadybeen.append( currentnode)
                print( currentnode.value )
                thestack.append(currentnode.right)     
        else:
            if currentnode not in alreadybeen:#gets the rest of the nodes
                alreadybeen.append( currentnode)
                print( currentnode.value )
            
            thestack.pop()#ends the loop as the thestack becomes empty 
    print ()        

if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  #postorder(t)
  in_order1 (t)
