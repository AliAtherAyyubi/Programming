
class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert after a node
    def insert(self,head,data):
        self.new_node = Node(data)
        temp=True
        while temp:
            if self.head==None:
                self.head==self.new_node
                temp=False
            else:
                self.head=head.next

    
    def foo(self,start):
        if self.start == None:
            return
 
        print(self.start.data)
 
        if (start.next != None):
            self.foo(start.next.next)
 
        print(start.value)

    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next




if __name__ == '__main__':

    list = LinkedList()

    list.insert(list.head,56)
    list.insert(list.head,80)
    list.insert(list.head,18)
    list.insert(list.head,86)
    list.insert(list.head,20)
    list.insert(list.head,29)

    list.printList()



    