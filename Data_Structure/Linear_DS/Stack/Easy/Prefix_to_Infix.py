# ========================== Prefix to Infix Conversion ================================

# Infix : An expression is called the Infix expression if the operator appears in between the operands in the expression. Simply of the form (operand1 operator operand2). 
# Example : (A+B) * (C-D)

# Prefix : An expression is called the prefix expression if the operator appears in the expression before the operands. Simply of the form (operator operand1 operand2). 
# Example : *+AB-CD (Infix : (A+B) * (C-D) )

# Given a Prefix expression, convert it into a Infix expression. 
# Computers usually does the computation in either prefix or postfix (usually postfix). But for humans, its easier to understand an Infix expression rather than a prefix. Hence conversion is need for human understanding.

# Examples: 

# Input :  Prefix :  *+AB-CD
# Output : Infix : ((A+B)*(C-D))

# Input :  Prefix :  *-A/BC-/AKL
# Output : Infix : ((A-(B/C))*((A/K)-L))

def Prefix_to_Infix(s):
    st = []
    n = len(s)

    for c in range(n-1, -1, -1):
        if ('a' <= s[c] <= 'z') or ('A' <= s[c] <= 'Z') or ('0' <= s[c] <= '9'):
            st.append(s[c])
        elif s[c] == '*' or s[c] == '/' or s[c] == '+' or s[c] == '-' or s[c] == '^':
            x = st.pop()
            y = st.pop()
            exp = "(" + x + s[c] + y + ")"
            # print("exp ", exp)
            st.append(exp)
    
    return "".join(st)


if __name__ == "__main__":
    expression = "*+AB-CD"
    # expression = "*-A/BC-/AKL"
    print("OG ", expression)
    print("-----------------------------------------")
    print("Result", Prefix_to_Infix(expression))
