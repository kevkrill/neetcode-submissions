from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        common = count.most_common(k)

        res = []

        for num, freq in common:
            res.append(num)

        return res  
