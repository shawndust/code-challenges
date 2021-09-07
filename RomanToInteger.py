class Solution:
    def romanToInt(self, s: str) -> int:
        strMod = s
        sumTot = 0
        i = 0
        while i < len(strMod):
            if strMod[i] == 'M':
                sumTot = sumTot + 1000
            elif strMod[i] == 'D':
                sumTot = sumTot + 500
            elif strMod[i] == 'C':
                if i < len(strMod) - 1:
                    if strMod[i+1] == "M":
                        sumTot = sumTot + 900
                        i = i + 1
                    elif strMod[i+1] == "D":
                        sumTot = sumTot + 400
                        i = i + 1
                    else:
                        sumTot = sumTot + 100
                else:
                    sumTot = sumTot + 100
            elif strMod[i] == 'L':
                sumTot = sumTot + 50
            elif strMod[i] == 'X':
                if i < len(strMod) - 1:
                    if strMod[i+1]== 'L':
                        sumTot = sumTot + 40
                        i = i + 1
                    elif strMod[i+1] == 'C':
                        sumTot = sumTot + 90
                        i = i + 1
                    else:
                        sumTot = sumTot + 10
                else:
                    sumTot = sumTot + 10
            elif strMod[i] == 'V':
                sumTot = sumTot + 5
            elif strMod[i] == 'I':
                if i < len(strMod) - 1:
                    if strMod[i+1] == 'X':
                        sumTot = sumTot + 9
                        i = i + 1
                    elif strMod[i+1] == 'V':
                        sumTot = sumTot + 4
                        i = i + 1
                    else:
                        sumTot = sumTot + 1
                else: 
                    sumTot = sumTot + 1
            i = i + 1
        return sumTot
