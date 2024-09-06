from listQueue import *

class stacktoqueue:
    def __init__(self):
        self.__q=ListQueue()
        self.__tq=ListQueue()

    def moveelements(self,q,tq):
        while not q.isEmpty():
            tq.enqueue(q.dequeue())

    def push(self,x):
        self.moveelements(self.__q,self.__tq)
        self.__q.enqueue(x)
        self.moveelements(self.__tq,self.__q)

    def pop(self):
        return self.__q.dequeue()
    
