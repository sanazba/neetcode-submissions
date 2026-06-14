class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res =[1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *=nums[i]
### مرحله 2: محاسبه postfix (حاصل‌ضرب از راست)
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
#range(start, stop, step)
#start = len(nums) - 1: شروع از آخرین ایندکس
#stop = -1: توقف قبل از -1 (یعنی تا ایندکس 0)
#step = -1: هر بار یک قدم به عقب

