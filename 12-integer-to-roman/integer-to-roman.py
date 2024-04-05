class Solution:
    def intToRoman(self, num: int) -> str:
        hMap={
            "I" : 1,
            "IV": 4,
            "V" : 5,
            "IX": 9,
            "X" : 10,
            "XL": 40,
            "L" : 50,
            "XC": 90,
            "C" :100,
            "CD":400,
            "D" :500,
            "CM":900,
            "M":1000,
        }
        STR=""
        while num!=0:
            for h in reversed(hMap.keys()):
                if hMap[h]<=num:
                    num-=hMap[h]
                    STR+=h
                    break
        return STR
