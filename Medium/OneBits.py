def getOneBits(n):
    def findTheBitArray(n):
        bitTable = []
        tempNum = 0
        powerNum = 0

        while n > tempNum:
            tempNum = pow(2, powerNum)
            if n < tempNum:
                break
            bitTable.append(tempNum)
            powerNum += 1
        reverseBitTable = list(reversed(bitTable))
        return reverseBitTable
    
    bitTable = findTheBitArray(n)
    cnt = 0
    result = []
    result.append(cnt)

    for num in range(0, len(bitTable)):
        if n - bitTable[num] >= 0:
            n = n - bitTable[num]
            cnt += 1
            result[0] = cnt
            result.append(num + 1)

    return result

if __name__ == '__main__':
    bit = 168

    print(getOneBits(bit))