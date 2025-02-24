# two_pointers Problems

This folder contains solutions to various two_pointers-related coding problems.

##Array intersection 
Two pointers: look for triggers 
###Things we did good: 
    * Look for triggers; sorted, duplicates 
    * Found brute force solution 
###Things we need to remember 
    * How to optimize; figure out how to use two pointer and why my solution was
     not optimized, missed that my brute force was o(n^2) 
    * When comparing two arrays the two pointers need to less then the length of
     the array they are iterating through 
    * If the values at the pointers are less; remember since they are sorted 
    that means we need to move the left pointer + 1 
    * If the values at the pointer are greater than move the right pointer - 1 
 
##Reverse Case Match 
###Things we did good: 
    * Broke down the problem well and understood what we wanted to do 
 
 
###Things we need to remember  
    * Use pointers 
    * Check if I is incrementing the index or element 
    * Remember how to use for i in range 
    * Reverse a string for a string is s[::-1] and .reverse() for an array 
    * However, using two pointers we don’t need those at all 
    * Simple solution is to only compare the values at upper/lower as you pass 
    them then to compare make one upper/lower first 
    * Look at big o! 
    * Use loop invariants, like l = 0 and r = len(s) - 1 
    * Edge cases; empty string/array, string/array = 1 
    * Draw the pointers out 
        * Short input that exercises every case anaylysis 
        * Input for each possible way to exit loop 
 
With two pointers, think simpler, we can skip, compare, swap, write values, 
and we can make those values upper or lower is needed, isupper() and islower() 
 
##Merge Two Sorted Arrays 
###Things we did good: 
    * Came up with a working solution 
###Things we need to remember  
    * Recognize the need for two pointers(look at triggers) 
    * Get used to implementing two pointer techniques  
    * Sorted returns a new list, its slower and not as good,  
    * Sort modifies the list, faster, returns none 
    * Neither of these are better than two pointer tho so learn it 
    * Practice big(o) - got it wrong again for my solution 
 
##Two Sum 
###Things we did good: 
    * Recognized that we can use nested loops to solve but that’s not optimal, 
    a dict would be better for loop 
###Things we need to remember  
    * Coming up with big(o) 
    * How enumerate works, what values are I and num when using it 
    * dict[number] = value; this looks like {number: value} 
 
##3 way merge without duplicates 
###Things we did good: 
    * It was the right idea to use same approach as two merged array 
    * Noticed we needed a unique data structure and that it should be sorted 
###Things we need to remember  
    * How to implement sorting without sort function, comparison of values at 
    the pointers 
    * bigo(n) 
    * To solve use the idea of merge two sorted arrays, merge two and then when 
    you have those merged, merge the last one  
    * Use geeks for geeks and go over this solution 
 
##Sort Valley-shaped array 
###Things we did good: 
    * We tried 
###Things we need to remember  
    * Reread and work to understand the problem! 
    * Do brute force before trying to optimize 
    * Think how to solve this intuitively and think about what info we are given 
 
##Missing numbers in range 
###Things we did good: 
    * Came up with a brute force solution 
###Things we need to remember  
    * Think of sets, they provide instant look ups. To use a set just
     arr_set = set() 
    * Ask yourself what DS can I use here? 
    * If I’m iterating over a whole list, ask can I just do what is missing? 
    Or over the specific values I want… 
    * n^2, work on finding an optimal solution… 
    * Don’t do unnecessary iterations(think sets) 
Gaps in understanding: 
    1. Data structure trade-offs: Understand the pros and cons of different 
    data structures (e.g., lists, sets, dictionaries). In this case, using a 
    set provided faster lookups. 
    2. Algorithmic complexity: Familiarize yourself with Big O notation and 
    practice analyzing the time and space complexity of your solutions. 
    3. Problem decomposition: Break down problems into smaller sub-problems 
    and identify opportunities for optimization. 
Advice: 
    1. Practice consistently: Regularly solve problems on LeetCode or other 
    platforms to develop your problem-solving skills. 
    2. Analyze your solutions: Take the time to review your code, identify areas
     for improvement, and optimize your solutions. 
    3. Learn from others: Study solutions from experienced coders, and try to 
    understand their thought process and design decisions. 
    4. Focus on fundamentals: Make sure you have a solid grasp of basic data 
    structures, algorithms, and software engineering principles. 
 
##Interval intersection 
###Things we did good: 
    * We did pseudocode to try and work through the problem 
    * We understood the problem 
###Things we need to remember  
    * Put more pieces together in the problem to see the bigger picture 
    * Think about two pointer approaches more and get better and solving them 
    * Work through the problem  
    * Again look at edge cases! 
