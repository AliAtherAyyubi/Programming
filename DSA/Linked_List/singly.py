

class Node:
    def __init__(self,data):
        self.item=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None


if __name__=='__main__':

    list= LinkedList()

    list.head= Node(1)
    second= Node(2)
    third= Node(3)

    list.head.next=second
    second.next=third

    # print(list.head.item)
    # print(list.head.next.item)
    # print(list.head.next.next.item)

    while list.head!=None:
        print(list.head.item)
        list.head= list.head.next


