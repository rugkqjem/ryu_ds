from liststack import*
def evaluate(p):
    s=ListStack()
    digitPreviously=False #앞이 숫자인지
    for i in p:
        if i.isdigit():
            if digitPreviously:
                tmp=s.pop() #스택에 들어있던 거 (바로앞 연결되는 숫자)
                tmp=10*tmp+(ord(i)-ord('0'))
                s.push(tmp)
            else:
                s.push(ord(i)-ord('0'))
                digitPreviously=True
        elif isoperator(i):
            s.push(operation(s.pop(),s.pop(),i)) #x2,x1,연산자
            digitPreviously=True

        else:
            digitPreviously=False
    return s.pop()


def operation(x2,x1,opr):
    return {'+':x1+x2,"-":x1-x2,'*':x1*x2,"/":x1//x2}[opr]

def isoperator(ch):
    return (ch=="+" or ch=='-' or ch=='*' or ch=='/')

def main():
    postfix="700 3 47 + 6 * - 4 /"
    print("inputstring:",postfix)
    answer=evaluate(postfix)
    print("answer:",answer)


if __name__=="__main__":
    main()