# no return & no result => code_block실행 후 종료 (None 반환)
#함수의 마지막 부분에 return을 사용하지 않을 경우 함수안의 로직만 실행될 뿐
# 호출자에게는 None을 반환합니다 (즉, 아무값도 반환안함)

def my_sum(num1,num2):
  sum_all=num1+num2;

sum_result=my_sum(3,4)

print(sum_result)  #None
type(sum_result)  #None

#아래의 예제와 같이 하나의 함수 안에 2개의 return문을 사용할 수 있습니다.
