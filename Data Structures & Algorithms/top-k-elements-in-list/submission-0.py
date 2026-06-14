class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # Count frequencies
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Bucket the numbers by frequency
        for n, c in count.items():
            freq[c].append(n)

        res = []
        # Traverse from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res