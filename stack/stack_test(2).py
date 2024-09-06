from liststack import ListStack

def reverecheck(str):
    checklist=ListStack()

    for i in range(len(str)):
        
        if(str[i]=='$'):
            break
        checklist.push(str[i])

    for j in range(i+1,len(str)):
        if ((checklist.isEmpty())):
            return False
        if (checklist.pop()!=str[j]):
            return False
        
    if(checklist.isEmpty()): 
        return True
    
    else: return False

str=input("입력: ")
answer=reverecheck(str)
print(answer)