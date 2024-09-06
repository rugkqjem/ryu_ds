def shellsort(A):
    H=gapsequence(len(A))  #gap 수열
    for h in H:   #h 갭
        for k in range(h):
            stepinsertionsort(A,k,h)

def stepinsertionsort(A,k,h):
    for i in range(k+h,len(A),h):
        j=i-h  #j까지는 정렬 되어있는거임 insert정렬에서 loc같은거
        newitem=A[i]

        while 0<=j and newitem<A[j]:
            A[j+h]=A[j]
            j-=h

        A[j+h]=newitem

def gapsequence(n):
    H=[1];gap=1
    while gap<n/2:
        gap*=2
        H.append(gap)
    H.reverse()
    return H


# def gapsequence(n):
#     H=[1]; gap=1
#     while gap<n/5:
#         gap=3*gap+1
#         H.append(gap)
#     H.reverse()
#     return H



A=[1,23,43,22,45,76,2]
shellsort(A)
print(A)