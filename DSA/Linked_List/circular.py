

class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def insertFront(self,data):
        new_node= Node(data)

        if self.head is None:
            self.head= new_node

            return
        
        new_node.next=self.head

        while self.head:
            self.head=self.head.next

        self.head.next=new_node
        self.head=new_node

    def printList(self):
        current= self.head
        while current:
            print(current.data," ",end="")
            current=current.next
            if current is self.head:
                break

if __name__ == '__main__':

    list = LinkedList()

    # one= Node(1)
    # two= Node(2)
    # three= Node(3)

    # one.next=two
    # two.next=three
    # three.next=one

    # list.head=one

    list.insertFront(3)
    list.insertFront(5)
    list.insertFront(34)
    list.printList()