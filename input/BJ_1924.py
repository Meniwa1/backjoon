import datetime # datetime 모듈을 사용하기 위해 임폴트
x,y = input().split() #문자 두개를 받음
days = [ 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT','SUN'] # 요일 
x = int(x) # 인트 초기화
y = int(y)
b= days[datetime.date(2007,x,y).weekday()] #데이트 모듈의 함수 weekday 날짜 요일 정보를 0~6까지 리턴
print(b) #출력