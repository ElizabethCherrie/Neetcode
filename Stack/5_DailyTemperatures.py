"""Task 5 Daily Temperatures
You are given an array of integers temperatures where temperatures[i] 
represents the daily temperatures on the ith day.
Return an array result where result[i] is the number of days after the ith
day before a warmer temperature appears on a future day. If there is no day
 in the future where a warmer temperature will appear for the ith day, 
 set result[i] to 0 instead.
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range (len(temperatures)):
            tempreture = temperatures[i]
            while stack and tempreture > temperatures[stack[-1]]:
                day = stack.pop()
                result[day] = i - day
            stack.append(i)
        return result