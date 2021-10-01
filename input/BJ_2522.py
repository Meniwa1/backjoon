n = int(input())
star = '*'
blank = ' '
for i in range(1,n):
    print(blank * (n-i) + star*(i))
for i in range(n,0,-1):
    print(blank * (n-i) + star*(i))
