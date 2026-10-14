class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, max_length = 0, 0
        counts = {}

        for right,char in enumerate(s):
            counts[char] = counts.get(char,0) + 1
            max_freq = max(counts.values())
            window_len = right-left+1
            while (window_len - max_freq > k):
                left_char = s[left]
                counts[left_char] -= 1
                left += 1
                window_len -= 1
            max_length = max(max_length,window_len)
        return max_length
