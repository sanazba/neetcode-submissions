class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #	•	Stack خالی نیست
                stackT, stackInd = stack.pop() #آن روز قبلی را از Stack خارج می‌کنیم:

                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res


# i is index 	•	i → شماره روز
# t is temprature
# stack[-1] top of stack [0] is first place یعنی امروز، روز گرم‌ترِ آن روزی است که در بالای Stack قرار دارد
#اختلاف روزها را حساب می‌کنیم
#یعنی چند روز طول کشیده تا دمای گرم‌تر بیاید
