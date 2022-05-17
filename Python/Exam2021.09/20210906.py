# Nested Function

def generate_power(base_number):
    def nth_power(power):
        return base_number ** power
    return nth_power

calculate_power_of_two=generate_power(2)
calculate_power_of_two(7)

#decorator : 장식이라고 하는데, 함수위에 다른 함수를 골뱅이 마크를
#사용해서 장식처럼 달아놓는 것 (장식이 먼저 호출)
# decorator가 가능한 함수는 중첩함수만 가능하다

def is_paid_user(func):
    user_paid=True #간단화 하기 위해 무조건 true
    def wrapper(*args,**kwars):
        if user_paid:
            func()
        else:
            return
    return wrapper

@is_paid_user
def jackpot_stock_infomation():
    return "계시가 내려졌습니다. 삼성전자를 사세요"

#decorator를 이용해 Hello Welcome to wecode를 출력해보자
def welcome_decorator(num):
  def is_greeting_user(func):
    def wrapper():
        a=func()+num
        return a

    return wrapper
  return is_greeting_user

@welcome_decorator("Welcome to wecode!")
def greeting():
    return "Hello, "
greeting()

#self 이해하기
#첫번째 인자인 self에 대한 값은 파이썬이 자동으로 넘겨준다

class Foo:
    def func1():
        print("function1")
    def func2(self):
    #    print("function2")
        print(id(self))
        self.x=2
        print("function 2")
    def func3(self):
        u=self.x+1
        return 

Foo.func1()
f=Foo()
f.func2()
id(f)

import sys
print(sys.builtin_module_names)