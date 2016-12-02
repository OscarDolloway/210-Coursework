class Node:
    def __init__(self,name):
        self.name = name
        self.connections = []

    def __str__(self):
        return "{0} {1}".format(self.name, [x.name for x in self.connections])
        #return (self.name.connections)

class Graph:
    def __init__(self):
        self.list_node = {}
    def __str__(self):
        return ",".join([str(x) for x in self.list_node.items()])#vodoo
    
    def addnodes(self,name):
        if name in self.list_node:  #checks if node already exists: ensures we can only add 1 node
            return
        else:
            self.list_node[name] = Node(name) #adds node to name in the Node class
        #return (nodes)
          
    def addEdge(self,a,b):
        #checks if the said nodes exist, if they do we define them in the list_node
        if (a in self.list_node) and (b in self.list_node) and a!=b:#will not display if nodes connects to itself.
            nodea = self.list_node[a]
            nodeb = self.list_node[b]
            #we then establish the connection by appending to connection list,
            nodea.connections.append (nodeb)
            nodeb.connections.append (nodea)  #as its undirected we must do both nodes                                
nodes = Graph()
nodes.addnodes(1)
nodes.addnodes(2)
nodes.addnodes(3)
nodes.addnodes(4)
nodes.addnodes(5)
nodes.addnodes(6)

nodes.addEdge(1,2)
nodes.addEdge(1,3)
nodes.addEdge(3,4)
nodes.addEdge(4,5)
nodes.addEdge(6,5)
   
for item in nodes.list_node:
    print (str(nodes.list_node[item]))



#for item in nodes.list_node:
#    print (str(item) + "  " + str(nodes.list_node[item]))
