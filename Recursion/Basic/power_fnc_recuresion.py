# Power function using recursion
# pow(x, n) → x^n


def pow(x, n):
    if n == 0:
        return 1
    else:
        return x * pow(x,n-1)
    
print(pow(2,3))
