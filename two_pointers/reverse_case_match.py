'''Given a string s containing both uppercase and lowercase letters, determine 
if the lowercase letters match the uppercase letters in reverse order. In other 
words, check if the sequence of lowercase letters matches the sequence of 
uppercase letters when read backwards.


Example 1:
Input: s = "haDrRAHd"
Output: true
Explanation:
- Lowercase letters: "hard"
- Uppercase letters: "DRAH"
- When reversed, "DRAH" becomes "HARD", which matches "hard" ignoring case.

Example 2:
Input: s = "haHrARDd"
Output: false
Explanation:
- Lowercase letters: "hard"
- Uppercase letters: "HARD"
- When reversed, "HARD" becomes "DRAH", which doesn't match "hard".
'''

def reverse_case_match(s):
  l, r = 0, len(s) - 1
  while l < len(s) and r >= 0:
    if not s[l].islower():
      l += 1
    elif not s[r].isupper():
      r -= 1
    else:
      if s[l] != s[r].lower():
        return False
      l += 1
      r -= 1
  return True