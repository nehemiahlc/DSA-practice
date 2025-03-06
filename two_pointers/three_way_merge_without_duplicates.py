'''Example 1:
Input: 
arr1 = [2, 3, 3, 4, 5, 7]
arr2 = [3, 3, 9]
arr3 = [3, 3, 9]
Output: [2, 3, 4, 5, 7, 9]
Explanation: The value 3 appears multiple times in the input but only once in
the output.

Example 2:
Input:
arr1 = [1, 2, 3]
arr2 = [2, 3, 4]
arr3 = [3, 4, 5]
Output: [1, 2, 3, 4, 5]
Explanation: Each duplicate value is included only once.

Example 3:
Input:
arr1 = [1, 1, 1]
arr2 = [1, 1]
arr3 = [1]
Output: [1]
Explanation: All ones are merged into a single occurrence.'''

def three_way_merge(arr1, arr2, arr3):
  p1, p2, p3 = 0, 0, 0
  res = []
  while p1 < len(arr1) or p2 < len(arr2) or p3 < len(arr3):
    # Find the smallest value among current positions
    min_val = float('inf')
    if p1 < len(arr1):
      min_val = min(min_val, arr1[p1])
    if p2 < len(arr2):
      min_val = min(min_val, arr2[p2])
    if p3 < len(arr3):
      min_val = min(min_val, arr3[p3])

    # Skip duplicates of min_val in all arrays
    if p1 < len(arr1) and arr1[p1] == min_val:
      p1 += 1
    if p2 < len(arr2) and arr2[p2] == min_val:
      p2 += 1
    if p3 < len(arr3) and arr3[p3] == min_val:
      p3 += 1

    # Only add if we haven't added this value before
    if not res or res[-1] != min_val:
      res.append(min_val)

  return res