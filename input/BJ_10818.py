from typing import Deque

# 이게 정답이 아니네 ..;
n = int(input())

list_num = list(map(int, input().split()))
Deque(list_num,maxlen=n)
max = max(list_num)
min = min(list_num)
print(max,min)

'''n = input()
n = int(n)
list_num = list(map(int, input().split()))
if n >= len(list_num):
    max = max(list_num)
    min = min(list_num)
    print(max,min)


a = int(input())
b = list(map(int,input().split()))
print('{}{}'.format(min(b),max(b)))'''