# Complexity analysis 

### Bruteforce approach
Itertools.permutations generates $n!$ permutations. Then,  all of them is being checked using is_valid function
this function checks every pair of given list, so its complexity is $O(n^2)$
therefore, general complexity of brutforce method is $O(n! \cdot n^2)$

### Recursive approach
This algorithm don't generate all possible cases and do not check each one. Instead, we generate only right variants using recusrion with backtraking, so this method do not check LOTS of variants that alredy considered wrong. But in worst case we still need to check all possible permutations, so compplexity of this approach is $O(n!)$

### Fastest approach
This approach uses simple dictionary, where key of element is number of queens and value is solution for this number. So we need get 1 element from dict, and complexity of such action is $O(1)$
