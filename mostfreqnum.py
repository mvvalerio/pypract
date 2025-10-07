numList = [1,1,3,2,1,2,2,3,3,3,2]

freq = {}

for num in numList:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

maxFreq = max(freq.values())

mostFreq = [key for key, value in freq.items() if value == maxFreq]

print(f"The most frequent number is {mostFreq} with {maxFreq} appearances.")