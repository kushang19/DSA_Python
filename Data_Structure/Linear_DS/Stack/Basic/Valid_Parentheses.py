def ValidParentheses(s: str) -> bool:
    stack = []
    
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        # If opening bracket → push to stack
        if ch in '({[':
            stack.append(ch)

        # If closing bracket
        elif ch in ')}]':
            # Stack empty but closing bracket found
            if not stack:
                return False
            
            top = stack.pop()
            if pairs[ch] != top:
                return False

    # Stack must be empty at the end
    return len(stack) == 0



print(ValidParentheses("[{()}]"))