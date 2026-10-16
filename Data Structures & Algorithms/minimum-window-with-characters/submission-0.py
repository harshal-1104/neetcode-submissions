class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countT = {}
        for char in t:
            countT[char] = countT.get(char,0) + 1
        left, right, have, need, res, lengthOfMinWindow = 0, 0, 0, len(countT), [], float('inf')
        window = {}

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            if char in countT and window[char] == countT[char]:
                have += 1
            if have == need:
                while have == need:
                    if (right - left + 1 < lengthOfMinWindow):
                        lengthOfMinWindow = right - left + 1
                        res = [left, right]
                    window[s[left]] -= 1
                    
                    if s[left] in countT and window[s[left]] < countT[s[left]]:
                        have -= 1
                    
                    left += 1
                    
        return s[res[0]: res[1] + 1] if lengthOfMinWindow != float('inf') else ""


