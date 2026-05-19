class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = {}

        for s in strs:

            sorted_strs = ''.join(sorted(s))

            if sorted_strs in anagram_map:
                anagram_map[sorted_strs].append(s)
            else:
                anagram_map[sorted_strs] = [s]

        return list(anagram_map.values())