'''Problem 27.2 - Smaller Prefixes: Solution
Python
The naive solution would be to iterate over all values of k from 1 to n/2, and 
for each value, compute and compare the sums of the two prefixes. This would 
take O(n^2) time. Instead, we can use a slow pointer, sp, and a fast pointer, 
fp, where fp moves twice as fast as sp. '''


def smaller_prefixes(arr):
  sp, fp = 0, 0
  slow_sum, fast_sum = 0, 0
  while fp < len(arr):
    slow_sum += arr[sp]
    fast_sum += arr[fp] + arr[fp + 1]
    if slow_sum >= fast_sum:
      return False
    sp += 1
    fp += 2
  return True