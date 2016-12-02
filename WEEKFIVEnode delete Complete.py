class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None
 
class List(object):
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,node,x):
        #Not actually perfect: how do we prepend to an existing list?
        if node !=None:
            x.next=node.next
            node.next=x
            x.prev=node
            if x.next!=None:
                x.next.prev=x              
        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==node:
            self.tail=x
            
    def display(self):
        values=[]
        node=self.head
        while node!=None:
            values.append(str(node.value))
            node=node.next
        print ("List: ",",".join(values))


    def deleteNode (self,node):
          if node.prev!=0:#checks if previous node has a value
                node.prev.next = node.next#current node = next node
          else:
                self.head = node.next#else we set the head of the list as the current
                
          if node.next  != 0:#checks if next node exists
                node.next.prev = node.prev#if there is a node next, the current node is node.previous
          else:
                self.tail = node.prev#if no node next, current node is set as tail.
            
          
            
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.tail,Node(6))
    l.insert(l.head,Node(8))
    l.insert(l.head,Node(5))
    l.insert(l.head,Node(9))
    l.insert(l.head,Node(10))
    l.deleteNode(l.tail.prev)
    l.display()
#http://stackoverflow.com/questions/4654953/removing-a-node-from-a-linked-list

    
