class ListQueue:
    def __init__(self):
        self.__queue=[]

    def enquenue(self,x):
        self.__queue.append(x)

    def dequeue(self):
        return self.__queue.pop(0)
    
    def front(self):
        if self.isEmpty():
            return None
        else:
            return self.__queue[0]
        
    def isEmpty(self):
        return(len(self.__queue)==0)
    
    def dequeueAll(self):
        self.__queue.clear()
    
    def printQueue(self):
        print("Queue from front:",end=' ')
        for i in range(len(self.__queue)):
            print(self.__queue[i],end=' ')
        print()
from collections import deque

def is_valid_format(input_string):
    # 입력된 문자열을 큐에 넣음
    queue = deque(input_string)
    
    # 큐의 길이가 3 미만이거나 '$'가 없는 경우 잘못된 형식
    if len(queue) < 3 or '$' not in queue:
        return False
    
    # '$'를 기준으로 큐를 두 부분으로 나눔
    first_part = deque()
    while queue[0] != '$':
        first_part.append(queue.popleft())
    queue.popleft()  # '$' 제거
    second_part = queue
    
    # 앞뒤 부분이 같은지 확인
    return first_part == second_part

# 테스트
input_string = input("문자열을 입력하세요: ")
if is_valid_format(input_string):
    print("입력된 문자열은 올바른 형식입니다.")
else:
    print("입력된 문자열은 올바른 형식이 아닙니다.")


