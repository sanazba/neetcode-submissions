class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # این خط، لیست nums را به یک مجموعه (Set) تبدیل می‌کند.
        longest = 0

        for n in nums:
            # check if its the statt of sequence
            if(n-1) not in numSet: # اگر عدد قبلی وجود نداشت، این شروع دنباله است
                length=0
                while (n+length) in numSet: #این حلقه طول دنباله متوالی را از عدد n به بعد می‌شمارد.
                    length += 1
                longest = max(length , longest)
        return longest