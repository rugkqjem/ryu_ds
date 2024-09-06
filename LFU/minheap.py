class minheap:

    def __init__(self,*args):
        if len(args)!=0:
            self.__A=args[0]
        else:
            self.__A=[]

    def insert(self,x):
        self.__A.append(x)
        i=len(self.__A)-1
        self.percolateUp(i)

    def percolateUp(self,i):
        parent=(i-1)//2
        if i>0 and self.__A[i]<self.__A[parent]:
            self.__A[i],self.__A[parent]=self.__A[parent],self.__A[i]
            self.percolateUp(parent)

    def deleteMin(self):
        min=self.__A[0]
        self.__A[0]=self.__A.pop()
        self.percolateDown(0)
        return min

    def percolateDown(self,i):
        child=2*i+1
        right=2*i+2
        if child<=len(self.__A)-1 :
            if right<=len(self.__A)-1 and self.__A[right]<self.__A[child]:
                child=right
            if self.__A[i]>self.__A[child]:
                self.__A[i],self.__A[child]=self.__A[child],self.__A[i]
                self.percolateDown(child)
    
    def isEmpty(self):
        return len(self.__A)==0
    
    def clear(self):
        self.__A=[]
    def size(self):
        return len(self.__A)

