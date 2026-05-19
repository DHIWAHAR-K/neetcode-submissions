class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        x = {}

        for i in s:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1
        
        y = {}

        for i in t:
            if i in y:
                y[i] += 1
            else:
                y[i] = 1
        
        return x == y