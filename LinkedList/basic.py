class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    

class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    
    def isEmpty(self):
        return self.head is None
    

    def display(self):
        if self.isEmpty():
            return "Linked list is empty"
        
        current=self.head
        elements=[]
        while current:
            elements.append(str(current.data))
            current=current.next
        print("->".join(elements)+"-> None")
    
    def insertAtBegnning(self,data):
        newNode=Node(data)

        newNode.next=self.head
        self.head=newNode
        self.size+=1


obj=LinkedList()

obj.insertAtBegnning(1)
obj.insertAtBegnning(2)
obj.insertAtBegnning(3)
obj.insertAtBegnning(4)

obj.display()