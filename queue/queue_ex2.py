from listQueue import *
#queue 실습 문제 (1)

def check(str):
    q=ListQueue()
    index=0
    for i in range(len(str)):
        if str[i]=='$': index=i+1 ; break
        q.enqueue(str[i])
        index+=1

    while not (q.isEmpty()) and q.dequeue()==str[index]:
        index+=1

    if q.isEmpty(): return True
    else: return False


str=input("문자열$문자열 check:")
answer=check(str)
print(answer)