class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum(): #تابع isalnum() بررسی می‌کند آیا کاراکتر، حرف یا عدد است یا نه.
                newStr += c.lower() # اگر کاراکتر مجاز بود، آن را به حروف کوچک تبدیل می‌کند (lower()) و به انتهای newStr اضافه می‌کند.
        return newStr == newStr[::-1]