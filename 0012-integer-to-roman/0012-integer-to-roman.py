class Solution:
    def intToRoman(self, num: int) -> str:
        Python
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = []
        for i, val in enumerate(values):
            if num == 0:
                break
            count, num = divmod(num, val)
            res.append(symbols[i] * count)
        return "".join(res)