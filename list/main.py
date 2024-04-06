from linkedBasic import LinkedListBasic
from listNode import ListNode
from circularLinkedList import *

list=CircularLinkedList()
list.append(30)
list.insert(0,20)
a=[4,3,3,2,1]
list.extend(a)
list.reverse()
list.pop(0)

list.printList()

if __name__=="__main__":

    names=["Amy","Kevin","Mary","David"]
    name_list=LinkedListBasic()

    for name in names:
        name_list.append(name)

    for name in name_list:
        print(name)

    name_list.pop(-1)
    name_list.insert(0,"Rose")
    name_list.sort()
    name_list.printList()
