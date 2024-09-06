from listQueue import *

class ListStack:
    def __init__(self):
        self.__stack=[]

    def push(self,x):
        self.__stack.append(x)
    
    def pop(self):
        return self.__stack.pop()
    
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__stack[-1]
        
    def isEmpty(self)->bool:
        return not bool(self.__stack)
    
    def popAll(self):
        self.__stack.clear()

    def printStack(self):
        print("stack from top:",end=' ')
        for i in range(len(self.__stack)-1,-1,-1):
            print(self.__stack[i],end=' ')
        print()



def palindrome(str):
    s=ListStack()
    q=ListQueue()

    for i in range(len(str)):
        s.push(str[i])
        q.enqueue(str[i])

    while not s.isEmpty() and s.pop()==q.dequeue():
        {}

    return q.isEmpty()


def main():
    str=input("문자열:")
    if palindrome(str) : print("TRUE")
    else: print("false")

if __name__=="__main__":
    main()