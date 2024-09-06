def insert(A):
    for i in range(1,len(A)):
        newitem=A[i]
        loc=i-1
        while loc>=0 and newitem <A[loc]:
            A[loc+1]=A[loc]
            loc-=1

        A[loc+1]=newitem


    
A=[15,12,54,46,1,2,75]
insert(A)
print(A)

