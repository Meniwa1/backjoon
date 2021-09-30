n = int(input())
star = '*'
blank = ' '
for i in range(1,n):
    print(blank*(n-i)+(star+blank)*(i))

