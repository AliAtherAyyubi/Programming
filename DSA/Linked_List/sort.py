

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

        # Sorting function
    
    def Sorting(self):
        current= self.head

        if(current==None):
            return
        else:
            while(current!=None):
                index= current.next
                while( index !=None):
                    if(current.data>index.data):
                        temp= current.data
                        current.data=index.data
                        index.data=temp
                    index= index.next
                current=current.next

    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next

if __name__ == '__main__':

    list = LinkedList()

    array = [56,80,18,86,20,29,40,21,78,1]

    for i in range(len(array)):
        list.insert(array[i])

    print("Unsorted LinkedList: ",end="")
    list.printList()

    list.Sorting()

    print("\n\nSorted LinkedList: ",end="")
    list.printList()


    