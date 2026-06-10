from collections import defaultdict 

nums = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]
freq = defaultdict(int)
for i in nums :
    freq[i] += 1
print(freq)
ans = 0 
for val in freq.values() :
    if val % 3 == 0 :
        ans += val // 3
    else :
        ans += val // 3 + 1
print(ans)