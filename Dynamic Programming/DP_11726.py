# dp = n-1 + n-2  점화식
n = int(input())
dp = [0 for _ in range(n+1)]
if n <= 3: # 1,2,3 일경우엔 n과 같음
    print(n)
else:
    dp [1] = 1
    dp [2] = 2
    for i in range(3,n+1) :
        dp[i] = dp[i-1] + dp[i-2] # 점화식
    print (dp[i] % 10007)