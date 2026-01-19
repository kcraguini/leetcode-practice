class Solution:
    def romanizer(self, numbers):
        romanizedNum = []

        # Hash map for all of the roman numerals
        mapping = {
            1000 : "M",
            900 : "CM",
            500 : "D",
            400 : "CD",
            100 : "C",
            90 : "XC",
            50 : "L",
            40 : "XL",
            10 : "X",
            9 : "IX",
            5 : "V",
            4 : "IV",
            1 : "I"
        }

        

        for number in numbers:
            tempRomanNum = []
            for value, symbol in mapping.items():
                count = number // value
                tempRomanNum.append(symbol * count)
                number -= count * value

            romanizedNum.append("".join(tempRomanNum))
        
        return romanizedNum
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.romanizer([600,32,10]))
    