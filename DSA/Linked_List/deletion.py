

class Node:
    def __init__(self,data):
        self.data= data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

# Insert into end
    def insert(self,data):
        new_node = Node(data)

        if self.head==None:
            self.head=new_node
            return
        
        last= self.head
        while (last.next):
            last=last.next

        last.next= new_node

        # delete function
    def deleteEnd(self):

        temp= self.head

        if temp==None:
            return
        
        while (temp.next.next!=None):
            temp=temp.next

        temp.next=None

    def deleteHead(self):
        # self.head=None
        self.head=self.head.next

    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next

if __name__ == '__main__':

    list = LinkedList()

    array = [56,80,18,86,20,29]

    for i in range(len(array)):
        list.insert(array[i])

    

    print('\n LinkedList: ')
    list.printList()

    # list.deleteEnd()
    # list.deleteEnd()

    # # print(list.head.next.next.data)
    # print('\Deleting from End: ')
    # list.printList()

    print('\nDeleting from Begin: ')
    list.deleteHead()
    list.printList()