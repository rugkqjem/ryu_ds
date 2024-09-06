def mergesort(A,p,r):
    if p<r:
        q=(p+r)//2
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p,q,r):
    i=p; j=q+1; t=0
    tmp=[0 for i in range(r-p+1)]

    while (i<=q and j<=r):
        if A[i]<=A[j]:
            tmp[t]=A[i]; t+=1; i+=1
        else:
            tmp[t]=A[j]; t+=1; j+=1
        
    while (i<=q):
        tmp[t]=A[i]; t+=1; i+=1

    while (j<=r):
        tmp[t]=A[j]; t+=1; j+=1

    t=0
    for k in range(p,r+1):
        A[k]=tmp[t];t+=1


    # i=p;t=0
    # while i<=r:
    #     A[i]=tmp[t]; t+=1; i+=1


A=[1,23,43,22,45,76,2]
mergesort(A,0,len(A)-1)
print(A)
