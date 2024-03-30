from listNode import ListNode

class LinkedListBasic:
    def __init__(self):
        self.__head=ListNode('dummy',None)
        self.__numItems=0

    def insert(self,i:int,newItem):
        if i>=0 and i<= self.__numItems:
            prev=self.__getNode(i-1)
            newNode=ListNode(newItem,prev.next)
            prev.next=newNode
            self.__numItems+=1

        else:
            print("index",i,":out of bound in insert()")

    def append(self,newItem):
        prev=self.__getNode(self.__numItems-1)
        newNode=ListNode(newItem,None)
        prev.next=newNode
        self.__numItems +=1

    def pop(self,i:int):
        if(i>=0 and i<=self.__numItems):
            prev=self.__getNode(i-1)
            curr=prev.next
            reItem=curr.item
            prev.next = curr.next
            self.__numItems-=1
            return reItem
        else:
            return None
        
    def get(self,i:int):
        if self.isEmpty():
            return None
        if (i>=0 and i<=self.__numItems-1):
            return self.__getNode(i).item
        else:
            return None
    def index(self,x)->int:
        curr=self.__head.next
        for index in range(self.__numItems):
            if curr.item==x:
                return index
            else:
                curr=curr.next
        return -2
    
    def sort(self)->None:
        a=[]
        for index in range(self.__numItems):
            a.append(self.get(index))
        a.sort()
        self.clear()
        for index in range(len(a)):
            self.append(a[index])

    def printList(self):
        curr=self.__head.next
        while curr !=None:
            print(curr.item,end=' ')
            curr=curr.next
        print()

    def __getNode(self, index: int):
        curr = self.__head
        for _ in range(index + 1):
            curr = curr.next
        return curr
    

    def __iter__(self):
        self.__iter_node = self.__head.next
        return self

    def __next__(self):
        if self.__iter_node is not None:
            item = self.__iter_node.item
            self.__iter_node = self.__iter_node.next
            return item
        else:
            raise StopIteration
        
    def isEmpty(self):
        return self.__numItems == 0

    def clear(self):
        self.__head.next = None
        self.__numItems = 0