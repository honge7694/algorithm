def numJewelsInStones(jewels: str, stones: str) -> int:
    result = {}
    count = 0

    for char in stones:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    for jewel in jewels:
        if jewel in result:
            count += result[jewel]
    
    return count

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
