from liststack import ListStack

def vs(str):
    st=ListStack()
    if str[0]==str[-1]:
        if str[1]==str[-2]:
            if str[2]==str[-3]:
                print("true")

        
    else:
        print("false")
    
def main():
    st=input()
    vs(st)

if __name__=="__main__":
    main()