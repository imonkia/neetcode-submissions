class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in seen:
                l = max(l, seen[char] + 1)
            seen[char] = i
            max_length = max(max_length, i - l + 1)
        
        return max_length