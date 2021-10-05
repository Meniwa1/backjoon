# 1,0은 횟수 0이다
# 1 + n-1 횟수
# 1 + n/2 횟수
# 1 + n/3 횟수
n = int(input())
count = 0
if n == 2 :
    count = 1
    print(count)
elif n <= 1:
    print(count)
elif n >2 :
    def dp(n):
        global count #전역변수
        if n % 2:
            n = int(n/3)
        else:
            n = int(n/2)
        count += 1
        if n > 1:
            dp(n)
        return count
    a = dp(n) + 1
    print(a)
'''def convertTo1(num):
    now = 1
    tries = 0
    check = [0 for _ in range(1,num + 1)]

    for i in range(0,num):
        tries = check[i]

        now_num = i + 1

        plus_one_index = now_num + 1 - 1
        mul_two_index = now_num * 2 - 1
        mul_three_index = now_num * 3 - 1

        if (plus_one_index) < num:
            if (check[plus_one_index] == 0) or (check[plus_one_index] > (tries + 1)):
                check[plus_one_index] = tries + 1

        if (mul_two_index) < num:
            if (check[mul_two_index] == 0) or (check[mul_two_index] > (tries + 1)):
                check[mul_two_index] = tries + 1

        if (mul_three_index) < num:
            if (check[mul_three_index] == 0) or (check[mul_three_index] > (tries + 1)):
                check[mul_three_index] = tries + 1

    return check[-1]'''

'''def dp(n):
    if n == 1:
        return 0
    if d[n] > 0:
        return d[n]
    d[n] = dp(n-1) + 1
    if n%2 == 0:
        temp = dp(n//2) + 1 # 나누기(/)로 하면 소수 나와서 오류생김
        if d[n] > temp:
            d[n] = temp
    if n%3 == 0:
        temp = dp(n//3) + 1
        if d[n] > temp:
            d[n] = temp
    return d[n]


n = int(input())
d = [0]*(n+1)
print(dp(n))'''