n = int(input())
star = '*'
blank = ' '
for i in range(0,n):
    print(blank * (i) + star *((2*n)-(i*2)-1))  
for i in range(n-1,0,-1):
    print(blank * (i-1) + star *((2*n)-(i*2)+1))