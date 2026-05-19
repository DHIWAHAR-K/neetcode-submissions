class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            count[x] = 1 + count.get(x, 0)
        
        arr = []
        for x, y in count.items():
            arr.append([y, x])
        
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        return result