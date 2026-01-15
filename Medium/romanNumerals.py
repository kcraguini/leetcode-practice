class Solution:
    def intToRoman(self, num: int) -> str:
        
                
        romanNumerals = []
        mapping = {
            1000:"M",
            900:"CM",
            500:"D",
            400:"CD",
            100:"C",
            90:"XC",
            50:"L",
            40:"XL",
            10:"X",
            9:"IX",
            5:"V",
            4:"IV",
            1:"I"
        }

        #mappingNums = [1000,500,100,50,10,5,1]

        for value, symbol in mapping.items():
            if num == 0:
                break
           
            count = num // value
            romanNumerals.append(symbol * count)
            num -= count * value

        return "".join(romanNumerals) 
    

if __name__ == '__main__':
    num = 1994
    sol = Solution()
    print(f"num: {num} in roman numerals is {sol.intToRoman(num)}")
    num = 58
    sol = Solution()
    print(f"num: {num} in roman numerals is {sol.intToRoman(num)}")
    num = 3
    sol = Solution()
    print(f"num: {num} in roman numerals is {sol.intToRoman(num)}")