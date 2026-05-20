class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for i in strs:
            key = "".join(sorted(i))
            if key in result:
                result[key].append(i)
            else:
                result[key] = [i]

        return list(result.values())