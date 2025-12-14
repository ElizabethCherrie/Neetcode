"""Task 2147. Number of Ways to Divide a Long Corridor

Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n
consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.

One room divider has already been installed to the left of index 0, and another to the right of index n - 1. 
Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.

Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. 
There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider 
installed in the first way but not in the second way.

Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7. If there is no way, return 0.

"""

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # Store 1000000007 in a variable for convenience
        MOD = 1_000_000_007

        # Initialize the array to store the result of each sub-problem
        count = [[-1] * 3 for _ in range(len(corridor) + 1)]

        # Base cases
        count[len(corridor)][0] = 0
        count[len(corridor)][1] = 0
        count[len(corridor)][2] = 1

        # Fill the array in a bottom-up fashion
        for index in range(len(corridor) - 1, -1, -1):
            if corridor[index] == "S":
                count[index][0] = count[index + 1][1]
                count[index][1] = count[index + 1][2]
                count[index][2] = count[index + 1][1]
            else:
                count[index][0] = count[index + 1][0]
                count[index][1] = count[index + 1][1]
                count[index][2] = (count[index + 1][0] + count[index + 1][2]) % MOD

        # Return the result
        return count[0][0]