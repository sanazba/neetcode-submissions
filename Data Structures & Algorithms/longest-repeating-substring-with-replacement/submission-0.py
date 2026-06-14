class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # تعداد هر کاراکتر در پنجره
        res = 0

        l = 0
        maxf = 0 # بیشترین تکرار یک کاراکتر

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])     # بیشترین تکرار یک کاراکتر در پنجره رو نگه‌دار

            while ( r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res
#این فرمول = طول پنجره  r-l+1
#count = {A: 3, B: 2}
# maxf = 3  ← چون A سه بار تکرار شده
