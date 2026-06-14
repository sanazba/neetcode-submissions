class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = Counter(s1)
        window = Counter(s2[:len(s1)]) #	یک Sliding Window به طول len(s1) روی s2 حرکت می‌دهیم


        if window == s1Count:
            return True

        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1 #حرفی که در موقعیت i است، وارد window شده ورود از راست
            window[s2[i - len(s1)]] -= 1 #حذف حرف قدیمی چون این حرفی است که از پنجره خارج می‌شود

            if window[s2[i - len(s1)]] == 0: #پس اگر شمارش صفر شد، باید کلید را حذف کنیم.
                del window[s2[i - len(s1)]]

            if window == s1Count:
                return True

        return False