class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums: # 1
            count[n] = 1 + count.get(n, 0) # {"1": 1}
        
        for n, c in count.items(): # key, value
            freq[c].append(n) # [[], [1]]

        res = []

        for i in range(len(freq) - 1, 0, -1): # reverse order
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res