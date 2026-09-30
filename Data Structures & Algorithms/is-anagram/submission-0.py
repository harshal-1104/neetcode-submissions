class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(s.split())
        t = "".join(t.split())

        if(len(s) != len(t)):
            return False
        return (sorted(s) == sorted(t))