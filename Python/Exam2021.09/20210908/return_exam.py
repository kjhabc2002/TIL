# no return & no result => code_block실행 후 종료 (None 반환)
#함수의 마지막 부분에 return을 사용하지 않을 경우 함수안의 로직만 실행될 뿐
# 호출자에게는 None을 반환합니다 (즉, 아무값도 반환안함)

def my_sum(num1,num2):
  sum_all=num1+num2;

sum_result=my_sum(3,4)

#print(sum_result)  #None
type(sum_result)  #None

#아래의 예제와 같이 하나의 함수 안에 2개의 return문을 사용할 수 있습니다.
#하지만 이럴경우엔 예기치않게 버그를 유발할 수도 있으므로 가급적 하나의 return문을
#사용하는 것이 좋습니다.

def my_abs(num):
      if num>0:
            return num
      elif num<0:
            return (-1)*num

abs_result=my_abs(0)
#argument에 0을 주게되면 return문이 실행되지 않고 그대로 None을 반환
#print(abs_result)
      
#return only ( no result ) => 함수즉시 종료
#마지막으로 return문만 있고 뒤에 result가 없는 경우입니다
# result에 반환값이 없으면 함수는 그대로 종료하게 됩니다.

def my_print(num):
  for i in range(1, num+1):
    print(i)
    if i == 3:
      return;

#print(my_print(3))  # 1,2,3,None

def open_account():
  print("새로운 계좌가 생성되었습니다")

#입금함수
def deposit(balance, money):
  print("입금이 완료되었습니다. 잔액은 {0}원입니다".format(balance+money))
  return balance+money

#출금함수
def withdraw(balance, money):
      if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-withdraw))
        return balance-money
      else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #w저녁에 출금
  commission=100 # 수수료 100원
  return commission, balance-money-commission 
  # return은 여러개의 값을 한번에 반환 가능 
  # 두개의 값을 튜플 형식으로 반환

balance=0 # 잔액 0원
balance=deposit(balance,1000)   #잔액은 1000원
balance=withdraw(balance, 2000) #잔액은 1000원 그대로
#balance=withdraw(balance,5000)
commission, balance=withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다. ".format(commission, balance))
