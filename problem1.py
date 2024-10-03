# Approach 1 - Recursive
# Time Complexity: O(2^n), where n is the amount

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         result = self.helper(coins, 0, amount, 0)
#         return result if result != float('inf') else -1

#     def helper(self, coins: List[int], i: int, amount: int, coinsUsed: int) -> int:
#         # base case
#         if amount == 0:
#             return coinsUsed
#         if amount < 0 or i >= len(coins):
#             return float('inf')

#         # logic
#         case0 = self.helper(coins, i + 1, amount, coinsUsed)
#         case1 = self.helper(coins, i, amount - coins[i], coinsUsed + 1)

#         return min(case0, case1)

# ---------------------------------------------------------------------------------------------

# Approach 2 - Dynamic Programming (2D Array)
# Time Complexity: O(m * n), where m is the number of coins and n is the target amount
# Space Complexity: O(m * n)

# import numpy as np

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         row = len(coins)
#         col = amount

#         # dp = np.zeros((row+1, col+1), dtype=int)
#         dp = [[0 for _ in range(col+1)] for _ in range(row+1)]

#         # Base case: 0 coins needed to make amount 0
#         for j in range(1, col+1):
#             dp[0][j] = float('inf')
        
#         for i in range(1, row+1):
#             for j in range(1, col+1):
#                 if j<coins[i-1]:
#                     dp[i][j] = dp[i-1][j]
#                 else:
#                     dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]])

#         if dp[row][col] == float('inf'):
#             return -1

#         return dp[row][col]

# ---------------------------------------------------------------------------------------------

# Approach 3 - Dynamic Programming (1D Array)
# Time Complexity: O(m * n)
# Space Complexity: O(n)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        row = len(coins)
        col = amount

        # dp = np.zeros((row+1, col+1), dtype=int)
        dp = [0] * (col+1) # [0 for _ in range(col+1)]

        # Base case: 0 coins needed to make amount 0
        for j in range(1, col+1):
            dp[j] = float('inf')
        
        for i in range(1, row+1):
            for j in range(1, col+1):
                if j >= coins[i-1]:
                    dp[j] = min(dp[j], 1+dp[j-coins[i-1]])

        if dp[col] == float('inf'):
            return -1

        return dp[col]