#1

def rod_cutting(lengths, prices, total_length):
    # Number of different lengths available
    n = len(lengths)
    
    # Create an array to store maximum price for each length up to total_length
    dp = [0] * (total_length + 1)
    
    for i in range(1, total_length + 1):
        max_val = 0
        for j in range(n):
            if lengths[j] <= i:
                max_val = max(max_val, prices[j] + dp[i - lengths[j]])
        dp[i] = max_val
    
    return dp[total_length]


lengths = [1, 2, 3, 4, 5]
prices = [1, 5, 8, 9, 13]
total_length = 5

print(rod_cutting(lengths, prices, total_length))  # resutls in 13





#2. 

# A top down approach solves a problem recursively and stores subproblems to avoid recalculation.
# A bottom up approach builds solutions from the smallest to largest subproblems iteratively with a table.
# Bottom up avoids stack overflow 



#3.

# A greedy approach makes the best local choice at each step without planning for the future.
# A divide and conquer approach breaks the problem into independent subproblems and solves each recursively.
# A dynamic programming approach solves overlapping subproblems and stores results to avoid recomputation.
# Greedy is fast and simple but may not give the optimal solution.
# Divide and conquer is efficient for independent tasks like sorting but doesn’t reuse repeated work.
# Dynamic programming guarantees an optimal solution but may use more time and memory.


#4.

# The lengths problem can be solved by dynamic programming, because it has overlapping subproblems.
# A greedy approach does not always give the correct result, because the best local cut isn’t always part of the best overall solution.
# A divide and conquer approach can solve it, but it's less efficient due to repeated subproblem calculations.
# So, dynamic programming is the best choice for this problem.