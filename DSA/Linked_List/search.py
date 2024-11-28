

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

        # Search function
    def search(self,key):
        
        current= self.head
        while(current!=None):
            if(current.data==key):
                return True
            current=current.next

        return False


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

    found= list.search(80)

    if(found):
        print("Element Found ")
    else:
        print("Element Not Found")


    