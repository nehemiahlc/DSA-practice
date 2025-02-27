'''Problem 27.3 - Array Intersection: Solution
Python
This is a two-pointer problem where we need to find elements that appear in both arrays. Since the arrays are sorted, we can walk through them simultaneously, comparing elements at each step.

The algorithm uses two pointers:

p1: current position in arr1
p2: current position in arr2
At each step:

If the elements at both pointers are equal:
Add the element to the result
Move both pointers forward
If the element in arr1 is smaller:
Move p1 forward (since we won't find this element in arr2)
If the element in arr2 is smaller:
Move p2 forward (since we won't find this element in arr1)
The key points are:

We only need to scan each array once
The result will automatically be in sorted order
We need to handle duplicates correctly
We stop when either array is exhausted
Empty arrays result in an empty intersection'''

def common_elements(arr1, arr2):
  p1, p2 = 0, 0
  res = []
  while p1 < len(arr1) and p2 < len(arr2):
    if arr1[p1] == arr2[p2]:
      res.append(arr1[p1])
      p1 += 1
      p2 += 1
    elif arr1[p1] < arr2[p2]:
      p1 += 1
    else:
      p2 += 1
  return res