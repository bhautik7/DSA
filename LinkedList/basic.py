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

    def getSize(self):
        return self.size
    

    def display(self):
        if self.isEmpty():
            return "Linked list is empty"
        
        current=self.head
        elements=[]
        while current:
            elements.append(str(current.data))
            current=current.next
        print("->".join(elements)+"-> None")
        print(f"size={self.getSize()}")
    
    def insertAtPos(self,data,pos):
        if pos<0 or pos>self.size:
            print("invalid position")
            return
        
        if pos==0:
            self.insertAtBegnning(data)
            return
        newNode=Node(data)

        temp=self.head

        cnt=1 
        while cnt!=pos:
            cnt+=1
            temp=temp.next
        newNode.next=temp.next
        temp.next=newNode
        self.size+=1
        
    
    def insertAtEnd(self,data):
        if self.size==0:
            self.insertAtBegnning(data)
            return
        newNode=Node(data)

        temp=self.head

        while temp.next != None:
            temp=temp.next
        temp.next=newNode
        newNode.next=None
        self.size+=1

    def insertAtBegnning(self,data):
        newNode=Node(data)

        newNode.next=self.head
        self.head=newNode
        self.size+=1

    def deleteAtStart(self):
        if self.isEmpty():
            print("list is empty")
            return
        
        temp=self.head
        self.head=temp.next
        self.size-=1
    
    def deleteAtEnd(self):
        if self.isEmpty():
            print("list is empty")
            return
        
        if self.head.next is None: #only one node
            self.head=None
            self.size-=1
            return

        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
        self.size-=1
    
    def deleteAtPos(self,pos):
        if self.isEmpty():
            print("list is empty")
            return
        if pos==1:#only one node
            self.head=None
            self.size-=1
            return
        
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        
        temp.next=temp.next.next
        self.size-=1
        
        

obj=LinkedList()

obj.insertAtEnd(1) #O(n)
obj.insertAtEnd(2)
obj.insertAtEnd(3)
obj.insertAtEnd(4)
obj.insertAtBegnning(5) #O(1)
obj.insertAtPos(6,2)
obj.insertAtBegnning(8)
obj.insertAtPos(7,3) #O(pos)

obj.display()
obj.deleteAtStart()
obj.display()
obj.deleteAtEnd()
obj.display()
obj.deleteAtPos(3)
obj.display()