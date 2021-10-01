n = int(input())
star = '*'
blank = ' '
for i in range(0,n):
    print(star*(i)+blank*(2*(n-i))+star*(i))
for i in range(n,0,-1):
    print(star*(i)+blank*(2*(n-i))+star*(i))