def bubblesorting(A):
    for elements_nums in range(len(A),0,-1):
        for i in range(0,elements_nums-1):
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]


A=[1,23,43,22,45,76,2]
bubblesorting(A)
print(A)