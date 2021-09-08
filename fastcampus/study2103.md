# 자바(java)

## ch 01. 자바 기초

c언어로 프로그램을 짰을 당시에는 c언어의 포인터로 메모리를 자주 핸들링하였기 때문에 시스템이 자주 다운되는 일이 잦았다고한다. (안정성 불안)  
그러면서 좀더 안정성이 높은 언어가 뭐가 있을까하다가 생겨난 언어가 자바언어이다.  
자바언어는 굉장히 안정성이 높은 언어로, 기존에 c언어가 가지고 있는 여러가지 모음이라던가 불안정적인 요소들을 없애면서 시스템을 다운시키는 일이 없어졌다.  
특징으로는 플랫폼(=운영체제)에 영향을 받지 않아 다양한 환경에서 사용할 수 있습니다.  
c언어파일을 만들때 .c파일이 생성이되는데 컴파일을 하였을때 윈도우에서 컴파일을 하였을때의 실행파일과 리눅스에서 실행하였을때의 실행파일이 다르게 생성이 되서 환경에 맞게 파일을 실행하여야 하는 불편함이 있다.  
즉 한곳에서 실행한다고해서 다른 운영체제에서 쓸수없다.

## ch 01. 자바 기초

### 이클립스 실행하기

- 패키지이름은 소문자로 써야한다.(통상적인규약)
- 클래스이름은 대문자로 시작해야한다. ex)Hello.java

### 변수는 변하는 수입니다.

변수는 언제쓰나요?

- 프로그램에서는 항상 변하는 값을 나타낼 필요가 있음
- 표현하려는 수에 맞는 데이터 타입(자료형)을 이용하여 변수 선언
- 표현하려는 자료가 숫자,문자,문자열 등 다양할 수 있으므로 그에 맞는 자료형을 사용

변수의 이름 만들때

```
변수 이름은 영문자(소문자,대문자)나 숫자로 사용할 수 있고, 특수문자 중에는 $와 _만 사용 ex) count100,_master

변수 이름의 시작은 숫자로 할수 없음 ex) 27days, 1abc (x)

자바에서 이미 사용하고 있는 예약어는 사용할 수 없음( while, break 등)

변수이름은 프로그램 내에서 사용되는 것이므로 그 용도에 맞고 가독성이 좋게 만드는 것이 중요
```

### 자료형(data type) - 정수는 어떻게 표현하나요?

기본자료형의 종류

```
정수형 : byte(1),short(2),int(3),long(4)
문자형 : shar(2)
실수형 : float(3),double(4)
논리형 : boolean(1)
```

정수 자료형의 종류와 크기

```
byte : -2(7승) ~ 2(7승)-1      -128(부호비트 빼서 7승) ~ 127(0부터시작이라서 -1)
short : -2(15승) ~ 2(15승)-1
int : -2(31승) ~ 2(31승)-1
```

### 자료형(data type) - 문자는 프로그램에서 어떻게 표현하여 사용하나요?

### - 문자도 정수로 표현합니다.

어떤 문자를 컴퓨터 내부에서 표현하기 위해 특정 정수 값을 정의하는데 다른말로 인코딩이라고 부릅니다.

```
ex) A를 인코딩하여 65로 변환하였다.   <-> 인코딩의 반대는 디코딩
```

문자세트 : 각 문자를 얼마로 표현할 것인지 코드값을 모아둔 것을 문자세트라고함

```
ex) ASKII,euc-kr,utf-8.utf-16
```

### - 자바에서는 문자가 어떻게 표현되나요?

자바는 문자를 나타내기 위해 전세계 표준인 unicode를 사용
utf-16 인코딩을 사용(모든 문자를 2바이트로 표시)

### - 문자형 변수 선언과 사용하기

문자를 위한 데이터 타입 char ch='A';

```
'A'와 "A" 는 전혀 다르므로 구분하자
'A'는 2byte크기를가진 문자이고, "A"는 문자열이다.
```

내부적으로 숫자로 표현되므로 숫자를 넣어도 문자가 출력될 수 있음  
다만, 음수는 쓸수없고 양수만 쓸수있다.  
char ch2=66;

### - 용어 정리참고

```
character set: 문자를 숫자로 변환한 값의 세트
encoding: 문자가 숫자로 변환되는 것
decoding: 숫자가 문자로 변환되는 것

ASKII code: 알파벳과 숫자, 특수 문자 등을 1바이트에 표현하는데 사용하는 문자세트
UNICODE: 전 세계 표준으로 만든 문자세트
UTF-8: 1바이트에서 4바이트까지 다양하게 문자를 표현할 수 있음
UTF-16: 2바이트로 문자를 표현
```

### 변하지 않는 상수와 리터럴, 변수의 형변환

### - 상수(constant) 선언하기

- 상수는 변하지 않는 수
- 원주률 3.14 ,1년 12개월 등
- final 예약어를 사용하여 선언
- 상수를 사용하면 변하지 않는 값을 반복하여 사용할 때 의미있는 문자로 인식하기 쉽고 혹, 변하더라도 선언한 부분만 변경하면 되므로 여러부분을 수정할 필요가 없음