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
- Ask yourself what DS can I use here? 
    * If I’m iterating over a whole list, ask can I just do what is missing? 
    Or over the specific values I want… 
    * n^2, work on finding an optimal solution… 
    * Don’t do unnecessary iterations(think sets) 
- Gaps in understanding: 
    1. Data structure trade-offs: Understand the pros and cons of different 
    data structures (e.g., lists, sets, dictionaries). In this case, using a 
    set provided faster lookups. 
    2. Algorithmic complexity: Familiarize yourself with Big O notation and 
    practice analyzing the time and space complexity of your solutions. 
    3. Problem decomposition: Break down problems into smaller sub-problems 
    and identify opportunities for optimization. 
- Advice: 
    1. Practice consistently: Regularly solve problems on LeetCode or other 
    platforms to develop your problem-solving skills. 
    2. Analyze your solutions: Take the time to review your code, identify areas
     for improvement, and optimize your solutions. 
    3. Learn from others: Study solutions from experienced coders, and try to 
    understand their thought process and design decisions. 
    4. Focus on fundamentals: Make sure you have a solid grasp of basic data 
    structures, algorithms, and software engineering principles. 

---
 
## Interval intersection 
### Things we did good: 
- We did pseudocode to try and work through the problem 
- We understood the problem 
### Things we need to remember  
- Put more pieces together in the problem to see the bigger picture 
- Think about two pointer approaches more and get better and solving them 
- Work through the problem  
- Again look at edge cases! 
