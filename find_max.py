a=list()
for i in range(10):
    a.append(int(input()))

print(a)
n=len(a)

def find_max_recursive(list,n):
    if n==1:
        
        return list[0]
    else:
       if list[0]>find_max_recursive(list[1:],n-1):
           return list[0]
       else: 
           return find_max_recursive(list[1:],n-1)
       
       #효율적 메모리 할당 / max 값 list[-1]으로 설정
       #max_rest=find_max_recursive(list,n-1)
       #if list[n-1]>max_rest:
        #return list[n-1]
       #else:
        #return max_rest

def find_max_iterative(list,n):
    max_value=list[0]
    for i in range(1,n):
        if max_value < list[i] :
            max_value = list[i]
    return max_value

print(find_max_recursive(a,n))
print(find_max_iterative(a,n))
    