class Node:
    data = None
    next_node = None
    
    
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f'This node contains {self.data}'

class LinkedList:
    def __init__(self) :
        self.head = None
    def is_empty (self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current !=None:
            current = current.next_node
            count+=1
        return count
    
    
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
        
    def insert(self, index, data):
        new_node = Node(data)
        current = self.head
        previous = None
        position = index
        while position>0:
            previous = current
            current = current.next_node
            position -=1
        previous.next_node = new_node
        new_node.next_node =current
        
        
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while not found:
            if(current.data==data):
                found = True
                previous.next_node = current.next_node
                return
            if(current!=None):
                previous = current
                current = current.next_node
            else:
                return None
                
            
            
            
            
        
    def __repr__(self):
        current = self.head
        content =[]
        while current!=None:
            content.append(f'{current.data}')
            current = current.next_node
        return ','.join(content)


            