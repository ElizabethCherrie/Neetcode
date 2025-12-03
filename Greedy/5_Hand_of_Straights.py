"""Task 5 Hand of Straights

You are given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize.

You want to rearrange the cards into groups so that each group is of size groupSize, and card values are consecutively increasing by 1.

Return true if it's possible to rearrange the cards in this way, otherwise, return false.
"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for num in hand:
            start = num       

            while count[start - 1]:
                start -= 1
            
            while count[start]: 
                count[start] -= 1
                for i in range(1, groupSize):  
                    if count[start + i] <= 0:
                        return False
                    if count[start + i] < count[start]:
                        return False

                    count[start + i] -= 1

        return True