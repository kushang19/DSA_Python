# Infix to Postfix Expression

# Given a string s representing an infix expression ("operand1 operator operand2" ), Convert it into its postfix notation ("operand1 operand2 operator").

# Note: The precedence order is as follows: (^) has the highest precedence and is evaluated from right to left, (* and /) come next with left to right associativity, and (+ and -) have the lowest precedence with left to right associativity.

# Input: s = "a*(b+c)/d"
# Output: abc+*d/   


def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def isRightAssociative(c):
    return c == '^'

def infixToPostfix(s):
    st = []
    res = []

    for c in s:
        # If operand, add to result
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            res.append(c)

        # If '(', push to stack
        elif c == '(':
            st.append('(')

        # If ')', pop until '('
        elif c == ')':
            while st and st[-1] != '(':
                res.append(st.pop())
            st.pop()

        # If operator
        else:
            # while st and st[-1] != '(' and (prec(st[-1]) > prec(c) or (prec(st[-1]) == prec(c) and not isRightAssociative(c))):

            while st and st[-1] != '(' and \
                (prec(st[-1]) > prec(c) or (prec(st[-1]) == prec(c) \
                                    and not isRightAssociative(c))):

            # Keep popping from the stack while ALL of these are true:
            # Stack is not empty (st)
            # Top of stack is not '(' (st[-1] != '(')
            # Top of stack operator has higher precedence than the current operator (prec(st[-1]) > prec(c)),
            # OR
            # Top of stack operator has the same precedence but is left-associative (prec(st[-1]) == prec(c) and not isRightAssociative(c)).


                res.append(st.pop())
            st.append(c)

    # Pop remaining operators
    while st:
        res.append(st.pop())

    return ''.join(res)

if __name__ == '__main__':
    exp = "a*(b+c)/d"
    print(infixToPostfix(exp))


    