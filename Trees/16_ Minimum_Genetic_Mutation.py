"""Task 16 Minimum Genetic Mutation
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one 
mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations.
 A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations 
needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.
"""

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        bank = set(bank)
        bank.add(startGene)
        mutation = ['A','C','G','T']
        visited = set()
        
        q = deque([(startGene, 0)])
        
        if endGene not in bank:
            return -1
        
        if not bank and startGene != endGene:
            return -1
            
        while q:
            curGene, depth = q.popleft()
            if curGene == endGene: 
                return depth
            
            if curGene not in bank:         
                continue
            
            for i in range(len(curGene)):
                for mut in mutation:
                    if curGene[i] != mut:
                        newGene = curGene[:i] + mut + curGene[i+1:]
                        if newGene not in visited:
                            visited.add(newGene)
                            q.append((newGene, depth+1))
                            
        return -1
        