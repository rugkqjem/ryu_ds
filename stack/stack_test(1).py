from liststack import ListStack

def reverse(str):
    restr=ListStack()
    for i in range(len(str)):
        restr.push(str[i])
    
    out=""
    while not restr.isEmpty():
        out+=restr.pop()
    
    return out

def re(str):
    stack=ListStack()
    for i in str:
        stack.push(i)
    out=''
    while not stack.isEmpty():
        out+=stack.pop()
    return out

str=input("reverse 하고싶은 문자 입력: ")
answer=reverse(str)
answer1=re(str)
# print("reverse:",answer)
print("re:",answer1)

