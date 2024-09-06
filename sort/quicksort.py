def quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)





def partition(A,p,r):

    value=A[r]
    #1구역 마지막원소 index 
    i=p-1

    #3구역 첫원소
    for j in range(p,r):
        if A[j]<value:
            i+=1
            A[i],A[j]=A[j],A[i]
    

    A[i+1],A[r]=A[r],A[i+1]
    return i+1


A=[1,23,43,22,45,76,2]
quicksort(A,0,len(A)-1)
print(A)
