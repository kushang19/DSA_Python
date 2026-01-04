def in_to_post(s):
    postfix = []
    stack = []

    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3
    }

    for ch in s:
        # Operand
        if ch.isalnum():
            postfix.append(ch)

        # Opening bracket
        elif ch == "(":
            stack.append(ch)

        # Closing bracket
        elif ch == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()  # remove '('

        # Operator
        else:
            while (
                stack
                and stack[-1] != "("
                and precedence.get(stack[-1], 0) >= precedence[ch]
                and ch != "^"  # handle right associativity of ^
            ):
                postfix.append(stack.pop())
            stack.append(ch)

    # Pop remaining operators
    while stack:
        postfix.append(stack.pop())

    return "".join(postfix)


print(in_to_post("a*(b+c)/d"))