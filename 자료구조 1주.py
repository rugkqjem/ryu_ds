#1번
def seq(n):
    if n==1: #공차가 3인 등차수열의 1번째 원소 1이라 가정 
        return 1
    else:
        return seq(n-1)+3
    
n=int(input('자연수 입력:'))
print(seq(n))

#=============================================================
def move(n,src,tmp,dest):

    if n==1:
        print("move %d from %c to %c" %(n,src,dest))
    else:
        move(n-1,src,dest,tmp)
        print("move %d from %c to %c" %(n,src,dest))
        move(n-1,tmp,src,dest)

move(3,'a','b','c')




# def hanoi(n,src,tmp,dest):
#     if n==1:
#         move(n,src,tmp,dest)
#     else:
#         hanoi(n-1,src,dest,tmp)
#         move(n,src,tmp,dest)
#         hanoi(n-1,tmp,src,dest)






#================================================================
#3:n을 입력으로 받아 2n 을 계산해주는 함수 pow2 (n) 을 재귀적으로 구현하라
n=int(input("n:"))
def pow2(n):
    if n==1:
        return 2
    else :
        return 2*pow2(n-1)
print("2의 %d제곱:%d"%(n,pow2(n)))

#4================================================================
num=[2,4,1,8,9,3]
def max(num,n):
    if n==1:
        if num[0]<num[1]:
            return num[1]
        else:
            return num[0]
        
    else:
        if num[n-1]<num[n]:
            num[n-1]=num[n]
            return max(num,n-1)
        else:
            return max(num,n-1)
        
print(max(num,len(num)-1))

print("====================")

num=[2,4,1,8,9,3]
def max(num,n):
    if n==1:
        return num[0]
    return num[0] if num[0]>max(num[1:],n-1) else max(num[1:],n-1)

print(max(num,len(num)-1))
