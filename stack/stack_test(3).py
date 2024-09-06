from liststack import ListStack

def paranBalance(str):
    list=ListStack()

    for i in range(len(str)):
        if (str[i]=='('):
            list.push(str[i])
        if (str[i]==')'):
            if list.isEmpty(): return False
            else: list.pop()
    
    if list.isEmpty(): return True
    else: return False
    #그냥 return list.isEmpty() 해도 됨. 

check1="((800/(3+5)*2)"
answer1=paranBalance(check1)
check2="(82+2) / 4)"
answer2=paranBalance(check2)

print("check1:",answer1)
print("check2:",answer2)