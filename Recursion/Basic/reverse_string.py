#=================================== Method 1 ================================================

# Write a recursive function to reverse a string.Write a recursive function to reverse a string.

s = "hello"

# Your way (backward recursion): start from the last character, move left, and collect.
def fun(s):
    n = len(s)
    def rev_fun(n):
        if n < 0:
            return ""
        else:
            return s[n] + rev_fun(n-1)
    return rev_fun(n-1)
    
print("name:",fun(s))



#=================================== Method 2 ================================================

# This way (forward recursion): start from the first character, reverse the rest, then append the first at the end.

def reverse(s):
    # Base case: empty string or single char is already reversed
    if len(s) <= 1:
        return s
    else:
        # Reverse the rest of the string (s[1:])
        # Then add the first character at the end
        return reverse(s[1:]) + s[0]

print("Reversed:", reverse("hello"))



# Step-by-step execution for "hello":

# reverse("hello")
# s[1:] = "ello"
# Call reverse("ello") + "h"

# reverse("ello")
# Call reverse("llo") + "e"

# reverse("llo")
# Call reverse("lo") + "l"

# reverse("lo")
# Call reverse("o") + "l"

# reverse("o")
# Base case → returns "o"

# Now unwind (combine results):

# reverse("o") → "o"
# reverse("lo") → "o" + "l" → "ol"
# reverse("llo") → "ol" + "l" → "oll"
# reverse("ello") → "oll" + "e" → "olle"
# reverse("hello") → "olle" + "h" → "olleh"