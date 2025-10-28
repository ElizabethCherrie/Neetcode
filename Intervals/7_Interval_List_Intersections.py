"""Task 7 Interval List Intersections
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] 
and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. 
For example, the intersection of [1, 3] and [2, 4] is [2, 3].

"""

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:         
        i = 0
        j = 0 
        res = []
        
        while i < len(firstList) and j < len(secondList):
            
            start = max(firstList[i][0], secondList[j][0])
            minStart = min(firstList[i][0], secondList[j][0])
            
            end = min(secondList[j][1], firstList[i][1])
            maxEnd = max(secondList[j][1], firstList[i][1])
     
            # No intersection  
            if end < start:
                if firstList[i][1] == end:
                    i+=1
                else:
                    j+=1
                continue
                
            if end >= start:
                res.append([start, end])    
                if end == firstList[i][1]:
                    i+=1
                else:
                    j+=1
        
        return res            
            
            