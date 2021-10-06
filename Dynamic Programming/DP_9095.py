# 점화식 : DP[N] = DP[N-1] + DP[N-2] + DP[N-3]..  5+ 4 + 3 12  # 1,2 일경우엔 n과 같음 # n 값이 3일땐  (1,1,1)(1,2)(2,1)(3) 
for _ in range(int(input())):
  n = int(input())
  dp = [1,2,4]
  if n <= 3: 
    print(dp[n-1])
  else:
    for i in range(3,n+1) : 
      dp.append(dp[i-1] + dp[i-2] + dp[i - 3])  # append 함수는 리스트의 끝에 값을 넣어준다. 값이 리스트일 경우 하나의 객체로 추가 됨.
    print (dp[i-1])