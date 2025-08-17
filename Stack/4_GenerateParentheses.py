"""Task 4 Generate Parentheses
You are given an integer n. Return all well-formed parentheses 
strings that you can generate with n pairs of parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        for _ in range(n + 1):
            stack.append([])
        stack[0] = [""] 
        for each_list in range(n+1):
            for ins_out in range(each_list):
                for left in stack[ins_out]:
                    for right in stack[each_list-ins_out-1]:
                        stack[each_list].append("(" + left + ")" + right)
        return stack[-1]