class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}

        for i in nums:

            if i in x:
                x[i] += 1
            else:
                x[i] = 1

        return sorted(x, key = lambda i:x[i], reverse = True)[:k]