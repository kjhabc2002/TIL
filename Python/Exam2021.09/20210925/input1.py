from datetime import datetime

# 정리
# 1. 사용자로부터 입력받기
# input("입력할 시 출력할 메세지")

# 2. 자료형변환
# 숫자형으로 변환
# int(데이터)

#사용자로부터 두개의 숫자를 입력받고, 더한 결과를 출력하기
print("실습문제1")
x=input("첫번째 숫자를 입력하세요>>>")
y=input("두번째 숫자를 입력하세요>>>")

# 자료형 확인하기 : type(x)
# str = string = 문자열
# 숫자형으로 변환
# int함수를 사용 : int(데이터)
print(type(x))
result= int(x) + int(y)
print(result)

# 사용자로부터 태어난 연도를 입력받으면,
# 현재 나이를 출력하기
print("실습문제2")
x=input("태어난 연도를 입력하세요>>>")

age=datetime.today().year-int(x) +1
print("현재나이는",age,"세 입니다.")