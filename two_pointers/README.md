# Two Pointers Problems

This folder contains solutions to various two-pointer-related coding problems.

---

## Array Intersection  

### Things We Did Well:
- Looked for triggers: sorted, duplicates  
- Found a brute force solution  

### Things to Remember:
- How to optimize: figure out how to use two pointers and why my solution was not optimized. Missed that my brute force was **O(n²)**.  
- When comparing two arrays, the two pointers need to be **less than** the length of the array they are iterating through.  
- If the values at the pointers are less: since they are sorted, move the left pointer `+1`.  
- If the values at the pointers are greater, move the right pointer `-1`.  

---

## Reverse Case Match  

### Things We Did Well:
- Broke down the problem well and understood what we wanted to do.  

### Things to Remember:
- Use pointers.  
- Check if `i` is incrementing the index or element.  
- Remember how to use `for i in range()`.  
- Reverse a string with `s[::-1]` and `.reverse()` for an array.  
- However, using two pointers, we don’t need those at all.  
- A simple solution is to **only compare** the values at `upper/lower` as you pass them; then to compare, make one `upper/lower` first.  
- Look at **Big O**!  
- Use loop invariants, like `l = 0` and `r = len(s) - 1`.  
- Consider edge cases: empty string/array, string/array length of 1.  
- Draw the pointers out.  
    - Use **short inputs** that exercise every case analysis.  
    - Test inputs for **each possible way** to exit the loop.  

**With two pointers, think simpler:** we can skip, compare, swap, write values, and modify values to upper or lower if needed using `isupper()` and `islower()`.  

---

## Merge Two Sorted Arrays  

### Things We Did Well:
- Came up with a working solution.  

### Things to Remember:
- Recognize the need for two pointers (**look for triggers**).  
- Get used to implementing two-pointer techniques.  
- `sorted()` returns a **new list** (slower, not as efficient).  
- `.sort()` modifies the list **in-place** (faster, returns `None`).  
- Neither of these is better than the **two-pointer approach**, so learn it!  
- **Practice Big O** - got it wrong again for my solution.  

---

## Two Sum  

### Things We Did Well:
- Recognized that we can use nested loops to solve it, but that's not optimal.  
- A **dictionary (hash map)** would be better for a loop.  

### Things to Remember:
- Correctly analyzing **Big O** complexity.  
- Understanding how `enumerate()` works—what values are `i` and `num` when using it.  
- `dict[number] = value` - This looks like `{number: value}`.  

---

## 3-Way Merge Without Duplicates  

### Things We Did Well:
- Had the right idea to use the same approach as merging two arrays.  
- Realized we needed a **unique data structure** and that the result should be sorted.  

### Things to Remember:
- How to implement **sorting without using `.sort()`**, by comparing values at the pointers.  
- The solution is **O(n)**.  
- To solve it:
    1. Use the **merge two sorted arrays** approach.  
    2. Merge **two** first, then merge the last one.  
- Use **GeeksForGeeks** and review this solution.  

---

## Sort Valley-Shaped Array  

### Things We Did Well:
- We tried.  

### Things to Remember:
- **Reread and truly understand the problem!**  
- Do a **brute force** approach before trying to optimize.  
- Think **intuitively**—what information are we given?  

---

## Missing Numbers in a Range  

### Things We Did Well:
- Came up with a brute force solution.  

### Things to Remember:
- **Think of sets**—they provide **instant lookups**. Use a set like this:  
  ```python
  arr_set = set()
