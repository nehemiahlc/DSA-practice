'''Given an array arr, modify it in-place to reverse the order of its elements.


Example 1:
Input: arr = ['h', 'e', 'l', 'l', 'o']
Output: ['o', 'l', 'l', 'e', 'h']
Explanation: Each element's position is swapped with its corresponding
position from the end.

Example 2:
Input: arr = ['a']
Output: ['a']
Explanation: An array with one element remains unchanged.

Example 3:
Input: arr = ['a', 'b', 'c', 'd']
Output: ['d', 'c', 'b', 'a']
Explanation: The first element becomes last, second becomes second-to-last,
and so on.
'''
def reverse(arr):
  l, r = 0, len(arr) - 1
  while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1
    
    return arr