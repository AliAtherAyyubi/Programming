
class Node:
    # Creating a node
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

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

    
    def foo(self,start):
        if start == None:
            return
 
        print(start.data)
 
        if (start.next != None):
            self.foo(start.next.next)
 
        print(start.data)

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

    list.printList()

    # print('\nHead of LinkedList: ',list.head.data)
    # list.foo(list.head)



    