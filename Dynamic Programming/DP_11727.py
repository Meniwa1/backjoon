# 점화식 : DP[N] = DP[N-1] + DP[N-2] + DP[N-3]..  5+ 4 + 3 12  # 1,2 일경우엔 n과 같음 # n 값이 3일땐  (1,1,1)(1,2)(2,1)(3) 
# dp = n-1 + n-2  점화식
n = int(input())
dp = [0 for _ in range(n+1)]
if n <= 1: # 1,2,3 일경우엔 n과 같음
  print(n)
elif n == 2:
  print(n+1) 
else:
    dp [1] = 1
    dp [2] = 3
    for i in range(3,n+1) :
        dp[i] = dp[i-1] + 2*dp[i-2]   # 점화식 앞서 푼 문제에 dp [i - 2] 가 두배가 되면 된다
    print (dp[i] % 10007) 