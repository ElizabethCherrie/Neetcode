"""Task 895. Maximum Frequency Stack
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
"""

class FreqStack:

    def __init__(self):
        self.levels = defaultdict(list)
        self.count = defaultdict(int)
        self.level = 0

    def push(self, val: int) -> None:
        l = self.count.get(val,0) + 1
        self.count[val] += 1
        
        if l > self.level:
            self.level = l
            
        self.levels[l].append(val)

    def pop(self) -> int:
        ret = self.levels[self.level].pop()
        self.count[ret] -= 1
        
        if not self.levels[self.level]:
            self.level -= 1
        
        return ret
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()