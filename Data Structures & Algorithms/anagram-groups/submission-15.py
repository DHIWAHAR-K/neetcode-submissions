class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = {}

        for s in strs:

            sorted_str = ''.join(sorted(s))

            if sorted_str in anagram:
                anagram[sorted_str].append(s)
            else:
                anagram[sorted_str] = [s]

        
        return list(anagram.values())