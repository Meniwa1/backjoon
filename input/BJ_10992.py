n = input()
n = int(n)
print(' '*(n-1)+'*')
for i in range(2,n):
    print( ' '*(n-i) + '*' + ' '*(2*i-3) + '*')
if n >1:
    print('*'*(2*n-1)  )


a = int(input())
star = '*'
blank = ' '
line = a*2-1
for i in range(a,0,-1):
 if i == a:
  print(blank*(line//2),end='')
  print(star)
 elif i == 1:
  print(star*line)
 else:
  print(blank*(i-1)+star,end='')
  print(blank*(line-i*2)+star)

#for i in range(시작숫자, 끝숫자, 간격):
#for i in range(시작숫자, 끝숫자):
#for i in range(끝숫자):