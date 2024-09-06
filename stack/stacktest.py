from liststack import *

def reverse(str):
    st=ListStack()
    for i in range(len(str)):
        st.push(str[i])
    out=""
    while not st.isEmpty():
        out+=st.pop()
    return out

def main():
    input="test seq 12345"
    answer=reverse(input)
    print("input str:",input)
    print("reversed string:",answer)

if __name__=="__main__":
    main()