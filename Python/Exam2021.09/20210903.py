a=1
s='span'
#s[0]='z'  

#TypeError: 'str' object does not support item assignment
# span 문자열은 불변성을 가지고 있으므로 수정이 불가하다

#문자열,숫자,튜플은 불변성을 가지고 있다.
# 수정이나 삭제가 불가능하다
#c='z'+s[1:]

d={"key1" :1, "key2":2}
#d["key1"]=10
d.get("key3")
type(d.get("key3"))
print(d)

def add(a,b):
    c=1;
    d=a+b;
    return d

# 범위 : LEGB (Local E Global Builtin) 규칙
# builtin메서드 : list(),
a=1
b=2
d="전역 변수"

def add(a,b):
    c=1
    print(d)

    return a+b
print(f"a : {a}")
print(f"b : {b}")

add(a,b)

# 1. 함수는 객체이기 때문에 변수에 할당이 가능하다.
# 2. 함수내에서 변수를 찾는 규칙은 Local -> Enclosiong -> Global -> Built-in (LEGB)

#closure란? 함수의 반환값으로 내부함수를 사용하는 함수

#Closure
# 함수의 값을 할당하는데 쓴다


def calculator(x, y):
    #non-local
    a=1
    b=2

    def add(a):
    #지역변수
        return x+y+a
    return add

# 


