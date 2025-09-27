def count_char(s, ch):
    n = len(s)
    def fun(n,count):
        if n < 0:
            return count
        else:
            if s[n] == ch:
                count += 1
            return fun(n-1, count)
    return fun(n-1, count=0)

print("Result ==> ", count_char("hello", "h"))