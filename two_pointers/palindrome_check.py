# Example 1: s = "level
# Output = true

# Example 2: 
s = "naan"
# Output: true

# Example 3: 
s1 = "hello"
# Output: false

def palindrome_check(s):
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

print(palindrome_check(s))
print(palindrome_check(s1))
        
