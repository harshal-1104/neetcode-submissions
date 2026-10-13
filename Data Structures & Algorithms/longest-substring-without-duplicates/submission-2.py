class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = {}
        left, right, max_length = 0, 0, 0

        for right,char in enumerate(s):
            if char in hashset and hashset[char] >= left:
                left = hashset[char] + 1
            hashset[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length