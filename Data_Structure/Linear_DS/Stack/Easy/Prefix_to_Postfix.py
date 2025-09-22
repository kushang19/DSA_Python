# ========================== Prefix to Postfix Conversion ================================

def Prefix_to_Postfix(s):
    st = []
    n = len(s)

    for c in range(n-1, -1, -1):
        if ('a' <= s[c] <= 'z') or ('A' <= s[c] <= 'Z') or ('0' <= s[c] <= '9'):
            st.append(s[c])
        elif s[c] == '*' or s[c] == '/' or s[c] == '+' or s[c] == '-' or s[c] == '^':
            exp =  st.pop() + st.pop() + s[c] 
            st.append(exp)
    
    return "".join(st)


if __name__ == "__main__":
    # expression = "*+AB-CD"
    # expression = "*-A/BC-/AKL"
    expression = "*-A/BC-/AKL"
    print("OG ", expression)
    print("-----------------------------------------")
    print("Result", Prefix_to_Postfix(expression))
