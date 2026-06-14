class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # HashMap mapping charCOunt to list of anagrams
        for s in strs:
            count = [0] * 26 # a...z
            for c in s: # every single character in each string
                count[ord(c) - ord('a')] += 1 # aski of current character - aski of lower character a
            res[tuple(count)].append(s) # group anagrams
        return list(res.values()) # فقط لیست‌های آناگرام‌ها رو برگردون (بدون کلیدها)



#a= 80 -> 0, 80-80
#b= 81 -> 1, 81-80
#+=1 how many character we 
        # برو تو خونه مربوط به حرف c
        # عدد اون خونه رو یکی زیاد کن
        # چون یک بار این حرف رو دیدیم
