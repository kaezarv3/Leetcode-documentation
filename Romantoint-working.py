# https://leetcode.com/problems/roman-to-integer/

''' This Question is for leetcode 
    Given a roman numeral, covert it to an integer '''

def romanToInt(s: str) -> int:
    romanDict = {"I": 1,"V": 5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    res = 0
    window = []
    if s in romanDict:
        return romanDict[s]
    if len(s) > 1:
        for ch in s:
            window.append(ch)
            if len(window) > 2:
                window = window[1:]
            res += romanDict[ch]
            if (ch == "V" or ch == "X") and window[0] == "I":
                res -= 2
            if (ch == "L" or ch == "C") and window[0] == "X":
                res -= 20
            if (ch == "D" or ch == "M") and window[0] == "C":
                    res -= 200
    return res
    
    
print(romanToInt("MCMXCIV"))

"""ADD TO THE GITHUB, This one was kinda easy. Maybe do like 25 easy ones and then start doing mediums then hards. do 25 each"""