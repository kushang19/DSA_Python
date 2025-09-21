def prec(c):
    if c == "^":
        return 3

    elif c =="*" or c =="/":
        return 2

    elif c == "+" or c == "-":
        return 1
    else:
        return -1

def rightAssociate(c):
    return c == "^"


def infix_to_postfix(s):

    st = []
    res = []

    for c in s:
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            res.append(c)
        elif c =='(':
            st.append('(')
        elif c == ')':
            while st and st[-1] != '(':
                res.append(st.pop())
            st.pop()
        else:
            while st and st[-1] != '(' and (prec(st[-1]) > prec(c) or (prec(st[-1]) == prec(c) and not rightAssociate(c))):
                res.append(st.pop())
            
            st.append(c)

    while st:
        res.append(st.pop())
    
    return "".join(res)



if __name__ == "__main__":
    exp = "a*(b+c)/d"
    print(infix_to_postfix(exp))  #Output: abc+*d/