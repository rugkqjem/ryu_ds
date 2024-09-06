def selectionsorting1(A):
    for last_index in range(len(A)-1,0,-1):
        k=find_max_index1(A,last_index)
        A[k],A[last_index]=A[last_index],A[k] #인덱스에 들어있던 값을 서로 바꿔줌 max 값이 last index 자리에 들어갈 수 있도록 
    
def find_max_index1(A,last_index):

    #일단 index=0 값이 최대라고 가정하고 연산시작 
    max_index=0

    for i in range(1,last_index+1):
        if A[max_index]<A[i]:
            max_index=i
        
    return max_index


def selectionsorting2(A):
    for start_index in range(len(A)):
        k=find_max_index2(A,start_index)
        A[k],A[start_index]=A[start_index],A[k]


def find_max_index2(A,start_index):
    max_index=start_index

    for i in range(start_index,len(A)):
        if A[max_index]<A[i]:
            max_index=i

    return max_index



A=[2,42,32,44,12,14]
selectionsorting1(A)
print(A)
selectionsorting2(A)
print(A)