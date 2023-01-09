n = int(input()) # KG

array = [3, 5]

dp = [ 5001 for i in range(n+1) ]

dp[0] = 0

for i in range(2) : #
    for j in range(array[i], n+1) : #
        if dp[j - array[i]] != 5001 :
            dp[j] = min(dp[j], dp[j-array[i]]+1)

if dp[n] == 5001 :
    print(-1)
else :
    print(dp[n])