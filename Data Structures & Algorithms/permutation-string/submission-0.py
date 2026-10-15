class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
     
        counts_s1 = {}
        counts_s2 = {}
        
        for char in s1:
            counts_s1[char] = counts_s1.get(char,0) + 1
        
        for i in range(len(s1)):
            counts_s2[s2[i]] = counts_s2.get(s2[i], 0) + 1
        
        if counts_s1 == counts_s2:
            return True
                
        else:
            for j in range(len(s1), len(s2)):
                counts_s2[s2[j - len(s1)]] -= 1
                if counts_s2[s2[j - len(s1)]] == 0:
                    del counts_s2[s2[j - len(s1)]] #key should not remain in dict if count drops to 0

                counts_s2[s2[j]] = counts_s2.get(s2[j],0) + 1 
                if counts_s1 == counts_s2:
                    return True
    
        return False
        