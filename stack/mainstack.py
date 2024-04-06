from liststack import ListStack

def reverse(str):
    st=ListStack()
    for i in range(len(str)):
        st.push(str[i])
    out=""
    while not st.isEmpty():
        out+=st.pop()
    return out

def main():
    input="Test seq 12345"
    answer=reverse(input)
    print("Input string:",input)
    print("Reversed string:",answer)

if __name__=="__main__":
    main()
