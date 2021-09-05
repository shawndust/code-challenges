class Solution:
    def intToRoman(self, num: int) -> str:
        outString = ""
        Num = num
        if Num >= 1000:
            M = Num // 1000
            outString+=M*"M"
            Num = Num - M * 1000
        if Num >= 900:
            outString+="CM"
            Num = Num - 900
        if Num >= 500:
            D = Num // 500
            outString+=D*"D"
            Num = Num - D * 500
        if Num >= 400:
            outString+="CD"
            Num = Num - 400
        if Num >= 100:
            C = Num // 100
            outString+=C*"C"
            Num = Num - C * 100
        if Num >= 90:
            outString+="XC"
            Num = Num - 90
        if Num >= 50:
            L = Num // 50
            outString+=L*"L"
            Num = Num - L * 50
        if Num >= 40:
            outString+="XL"
            Num = Num - 40
        if Num >= 10:
            X = Num // 10
            outString+=X*"X"
            Num = Num - X * 10
        if Num == 9:
            outString+="IX"
            Num = Num - 9
        if Num >= 5:
            V = Num // 5
            outString+=V*"V"
            Num = Num - V * 5
        if Num == 4:
            outString+="IV"
            Num = Num - 4
        if Num <= 3:
            I = Num // 1
            outString+=I*"I"
            Num = Num - I * 1
            
        return outString
