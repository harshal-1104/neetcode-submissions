import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r"[^a-zA-Z0-9]","",s).lower()
        return cleaned_text == cleaned_text[::-1]    