def max(num,n):
    if n==0:
        return num[0]
    elif num[-1]>max(num[:-1],n-1): return num[-1]
    else: return max(num[:-1],n-1)

num=[2,4,1,8,9,3]
print(max(num,len(num)-1))