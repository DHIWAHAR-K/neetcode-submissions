class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram = {}

        for s in strs:

            x = "".join(sorted(s))

            if x in anagram:
                anagram[x].append(s)
            else:
                anagram[x] = [s]

        
        return list(anagram.values())