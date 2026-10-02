class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        hashmap = [[] for i in range(len(nums)+1)]

        for i in nums:
            count[i] = 1 + count.get(i,0)
        for i,j in count.items():
            hashmap[j].append(i)

        ans= []
        for i in range(len(hashmap) - 1 , 0, -1):
            for j in hashmap[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans