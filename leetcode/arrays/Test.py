"00011001101"

# 0 -> [3,2,1]
# 1 -> [2,2,1]

def countPerfSubStrings(s):
    orderMap = {0, 1}
    for ch in s:
        orderMap[ch].append(1+orderMap.get(ch, 1))
    for value in orderMap.values():
        print(value)


countPerfSubStrings("00011001101")




