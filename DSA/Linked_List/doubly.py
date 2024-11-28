
class Node:
    # Creating a node
    def __init__(self, data):
        self.data = data
        self.prev=None
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert into end
    def insertFront(self,data):
        new_node= Node(data)
        
        new_node.next=self.head

        if self.head is not None:
            self.head.prev=new_node

        self.head=new_node

    def insertAtEnd(self,data):
        new_node= Node(data)

        if self.head is None:
            self.head=new_node
            return
        
        last=self.head
        while last.next:
            last=last.next

        last.next=new_node
        new_node.prev=last


    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next




if __name__ == '__main__':

    list = LinkedList()

    array = [56,80,18,86,20,29]

    for i in range(len(array)):
        list.insertAtEnd(array[i])

    list.insertFront(4)
    list.insertFront(45)

    print(list.head.next.next.next.data)

    list.printList()

    last=list.head
    while last.next:
        last=last.next

    print("\n",last.prev.prev.data)





    