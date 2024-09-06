
from liststack import *

def evaluate(p):
    s=ListStack()
    digitPreviously=False #이전 변수에서 숫자가 발생했는지를 확인하기 위한 부울 변수
    for i in range(len(p)):
        ch=p[i]
        if ch.isdigit():
            if digitPreviously:
                #숫자 합쳐주기 예를 들면 700 인데 여기는 한글자씩 받으니까 7받고 0받으면
                 #7,0,0을 700으로 만들어주는 과정 
                tmp=s.pop()
                tmp=10*tmp+(ord(ch)-ord('0'))
                s.push(tmp)
            else:
                #a문자를 숫자로 변환하는과정 
                #ord(ch) : ch의 유니코드 포인트 반환 - '0'의 유니코드 포인트를 빼주면 숫자가 됨 
                s.push(ord(ch)-ord('0'))
                digitPreviously=True

        elif isOperator(ch):
            s.push(operation(s.pop(),s.pop(),ch))
            digitPreviously=True

        else:
            digitPreviously=False
    return s.pop()

def isOperator(ch):
    return (ch=="+" or ch=="-" or ch=="*" or ch=='/')

def operation(opr2,opr1,ch):
    return {'+':opr1+opr2,'-':opr1-opr2,"*":opr1*opr2,"/":opr1//opr2}[ch]

def main():
    postfix="700 3 47 + 6 * - 4 /"
    print("inputstring:",postfix)
    answer=evaluate(postfix)
    print("answer:",answer)


if __name__=="__main__":
    main()