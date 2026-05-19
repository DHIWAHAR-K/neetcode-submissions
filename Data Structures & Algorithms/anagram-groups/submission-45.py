class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = defaultdict(list)

        for i in strs:

            word = "".join(sorted(i))
            x[word].append(i)

        return list(x.values())