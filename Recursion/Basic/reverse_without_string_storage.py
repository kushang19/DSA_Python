# Print a number in reverse without converting it to string or using extra storage
# Input: 1234 → Output: 4321

def rev_num(n):
    # print(n%10) #4
    # print(n//10) #123
    # print(1//10) #0

    if n == 0:
        return 
    else:
        print(n%10,end="")
        return rev_num(n//10)

num = 123456789
rev_num(num)


# METHOD 2 : Use a Helper Function

def rev(n):
    def helper(n,rev):
        if n == 0:
            return rev
        return helper(n//10, rev * 10 + n%10)
    return helper(n,0)
    
number = 1234
print("\n",rev(number))