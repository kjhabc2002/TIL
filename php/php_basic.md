## PHP

## PHP란 무엇인가?

- 주로 HTML 코드를 프로그래밍적으로 생성
- 서버쪽에서 실행되는 클라이언트 언어
- Personal Home Page Tools의 약자에서 PHP: Hypertext Preprocessor로 의미가 변경되었다.

### 서버와 클라이언트

![](./img/img1.png)

- 서버 : 정보를 제공하거나 요청에 대해서 응답

- 클라이언트 : 무언가를 요청하는 사람

- 웹브라우저=web client
  반대로 서버에 웹서버가 있을 것이라는 추정을 할 수 있다.

웹브라우저의 검색창에 url,domain 등등을 입력하고 검색하기를 누르면 서버컴퓨터가 위치하고 있는 주소로 가서 '웹서버'라고 하는 소프트웨어에게 요청을 하게 된다.

이 웹서버가 하는 일은 웹브라우저가 어떠한 특정한 페이지를 보여달라고 요청을 하게되면 그 요청에 의해서 응답하는 것이 웹서버가 하는 일이다.

web client의 구체적인 제품에는 파이어폭스,크롬,ie,사파리 등등이 있다.

웹서버의 구체적인 제품에는 아파치,IIS,nginx이 있다.

초창기의 인터넷에는 클라이언트가 요청을 하게되면 웹서버는 자기 컴퓨터에 저장되어 있는 HTML문서그대로 읽어와서 인터넷을 통해서 응답하는 것이 기본적인 웹의 초창기 모습이었다.

정적인 웹페이지를 벗어나기 위해 개발자들이 고안해낸 것이 CGI(Common Gateway Interface)인데, CGI를 사용함으로써 사용자가 요청한 것이 php문서라고 한다면 웹서버는 php엔진을 호출해서 사용자가 요청한 예를들어 topic.php파일을 의뢰를 한다. php엔진은 php파일의 문법에 따라 해석을 하고 그 결과를 웹서버에게 돌려준다. 그렇게해서 웹서버는 웹클라이언트에게 마치 html파일인 것처럼 전송하게 된다.

> CGI란? 서버와 외부스크립트 또는 프로그램가 상호작용할 때 이루어지면 입출력을 정의한 표준

### PHP의 특성

PHP : Hypertext(=HTML) Preprocessor(=전처리)
문서와 문서가 링크로 연결되어있다.

### PHP의 장점

- 웹에 최적화된 언어
- 웹개발에 필요한 수많은 로직들이 함수의 형태로 미리 제공됨
- 크로스플랫폼
- 거의 모든 데이터베이스를 지원
- 가장 많은 공개소프트웨어가 php로 만들어짐

### PHP 정보를 얻을 수 있는 곳

- [php공식홈페이지](http://php.net/)
- [국내최대의 php커뮤니티](http://phpschool.com/)

### PHP로 만들어진 솔루션들

- http://www.phpbb.com/
- http://www.phpmyadmin.net/home_page/index.php
- http://wordpress.com/
- http://www.xpressengine.com/
- http://www.textcube.org/

## 첫번째 PHP 에플리케이션

![](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/62/1773.png)

D:\Program_Files\wampstack\apache2\htdocs\firstapp경로의 helloworld.php실행

```
<?php
echo "Hello world";
?>
```

helloworld2.php실행

```
<html>
<body>
echo "Hello world";
<?php
echo "Hello world";
?>
</body>
</html>
```

## 서버측 언어를 사용하는 이유

![](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/62/1774.png)

초창기 웹서버와 웹브라우저를 고안한 사람이 팀버너스리 경이다.
초창기에는 웹서버와 웹브라우저로 이루어져 있던 단순한 구조였다. 웹사이트가 점점 성장하게 되면서 웹사이트에 있는 무수한 사용자들이 보게되고, 방문한 사람들이 직접 메세지를 작성한 것을 사이트에 전송해서 그 메세지가 다른사람들에 의해 열람될 수 있도록 하니까 이러한 것들을 웹서버만으로 처리하지 못하게 된다. 그래서 엔지니어들이 이러한 문제를 해결하기 위해서 고안된 것이 CGI이다.

http 란 웹브라우저와 웹서버가 서로 데이터를 주고받기 위한 통신규약
CGI란 웹서버와 서버사이드스크립트(php,py,java ...)가 서로 데이터를 주고받기 위한 통신규약

CGI를 거쳐가면서 서버사이드스크립트를 웹서버가 웹클라이언트에게 마치 html파일인 것처럼 전송하게 된다.

DB,Mysql,Oracle데이터베이스는 데이터를 저장하는 것에 특화되어 있는데 어떠한 블로그에 있는 포스팅의 제목,본문,댓글에 있는 정보들이 데이터베이스에 저장이 되어있다가 사용자가 어떤 웹페이지를 요청하게 되면 웹서버는 이 웹서버를 처리할 수 있는 언어에게 위임하게 되고 이 언어는 언어로 작성되어 있는 코드를 해석해서 웹서버로 돌려보내게 되는데 그 과정에서 데이터베이스에 있는 본문,제목,댓글과 같은 데이터를 사용하는 코드가 들어있다면 php,java,py언어들이 이 데이터베이스에 접속해서 이러한 정보들을 가져온 다음에 이 정보들을 html문서로 만든다음에 다시 웹서버로 돌려보낸다.

기본적으로 HTML은 한번 파일이 만들어지면 언제나 똑같이 동작하지만 PHP는 보다시피 프로그래밍적으로 웹 페이지를 생산할 능력이 있기 때문에 페이지를 새로고침할때마다 달라지는 동적인 웹페이지를 만들 수 있습니다.

즉, HTML은 정적입니다. 한번 코드를 작성하면 언제나 같은 웹페이지만 만들 수 있습니다. 하지만 PHP는 동적입니다. 원하는 것을 PHP문법에 따라 쓰면 PHP는 그렇게 동작해 최종적으로 웹 페이지를 생성해서 웹 브라우저에게 전송하게 된다는 것입니다. 한가지 기억해둘만한 점은 PHP코드의 시작과 끝을 알리는 기호 `<?php ~ ?>` 라는 것과 그 기호 안쪽은 PHP문법에 따라 처리되고, 그 기호 바깥쪽인 부분은 php문법이 아닌 그냥 그대로 출력된다는 점입니다.

## 설치

WAMP는 윈도우(Window),아파치(Apache),Mysql(데이터베이스시스템)에 php의 p를 딴 약자입니다.

설치사이트

- http://bitnami.com/stack/wamp

## 숫자와 문자

[숫자와 문자 예제](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/number.php)

## 변수

변수는 문자나 숫자 같은 값을 담는 컨테이너다. 여기에 담겨진 값은 다른 값으로 바꿀 수 있다. 변수는 마치 (사람이 쓰는 언어인) 자연어에서 대명사와 비슷한 역할을 한다.

### 변수의 선언

[변수 예제1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/variable1.php)

[변수 예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/variable2.php)

[변수 예제3](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/variable3.php)

[변수 예제4](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/variable4.php)

### 상수

상수(constant)는 변하지 않는 값이다.
`1=2;`
1은 2가 될 수 없기 때문에 상수이다. 필요에 따라서 사용자가 직접 상수를 정의 할 수도 있다. 아래 예제를 보자.

### 변수의 데이터타입

php는 다른 언어들과 다르게 변수에 담길 값의 데이터 형식을 미리 지정할 필요가 없다.

```
<html>
<body>
<?php
$a = 100;
$a = "test";
$a = array(1,2,3);
?>
</body>
</html>
```

위의 코드는 PHP에서는 아무런 문제가 없다. 이것은 PHP의 장점이면서 단점으로 이야기 되기도 한다. 즉 변수 \$a를 선언할 때 변수에 어떤 값이 들어가야 하는지 미리 지정 할 필요가 없다. 필요에 따라서 다른 형식의 데이터를 넣으면 변수의 데이터 형식이 자동으로 변경된다. 이것은 매우 편리 하지만, 변수에 어떠한 형식의 데이터가 담겨있는지를 예측할 수 없기 때문에 오류가 발생할 가능성이 높아지기도 한다.

### 가변변수

가변변수는 변수의 이름을 변수로 변경 할 수 있는 기능이다.

```
<html>
<body>
<?php
// 변수 $title값은 subject
$title = 'subject';
// $$title은 문자열 'PHP tutorial'가 변수 $title의 값이 아니라 변수 $subject의 값이다.
$$title = 'PHP tutorial';
echo $subject;
?>
</body>
</html>
```

변수의 이름을 동적으로 만들 수 있다는 점은 PHP가 가진 유연함을 보여준다.

## 연산자

## 비교 연산자

좌항과 우항을 비교해서 서로 값이 같다면 true 다르다면 false가 된다. '='가 두개인 것을 주의하자.
`==`

var_dump에 값을 넣으면 입력값을 출력하고, 그와 동시에 입력값의 데이터타입을 알려준다.

비교연산자 예제1

```
<html>
<body>
<?php
echo "1==2 : ";
var_dump(1==2);           #false
echo '<br />';
echo "1==1 : ";
var_dump(1==1);           #true
echo '<br />';
echo '"one"=="two" : ';
var_dump("one"=="two");   #false
echo '<br />';
echo '"one"=="one" : ';
var_dump("one"=="one");   #true
echo '<br />';
?>
</body>
</html>
```

결과

```
1==2 : bool(false)
1==1 : bool(true)
"one"=="two" : bool(false)
"one"=="one" : bool(true)
```

[비교연산자 예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/variable2.php)

[비교연산자 예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/variable2.php)

===는 좌항과 우항이 정확하게 같다는 의미이다. 양쪽항이 데이터 형식까지 정확하게 동일해야 같은것으로 인정한다.
[비교연산자 예제3](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/variable2.php)

## 입출력 그리고 폼과 HTTP

### 에플리케이션의 입력값과 폼

프로그램은 입력값을 가질 수 있다. 그리고 입력값에 따라서 동작방법이 달라지거나 입력된 값을 저장/삭제/출력 할 수 있다.

[비교연산자 예제3](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/ex1.php)

![](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/6/1785.png)

![](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/6/1782.png)

![](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/6/1783.png)

### HTML폼

form이란 사용자가 입력한 정보를 받아서 서버로 전송하기 위한 HTML의 태그이다. 사용자가 입력한 정보를 받는 UI를 입력 컨트롤이라고 하는데 위의 코드에는 id와 password를 입력 받는 입력 컨트롤이 포함되어 있다. 입력 컨트롤에 입력된 정보는 해당 컨트롤의 속성 name의 값을 이름으로 데이터가 서버로 전송된다.

[html폼 예제](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/ex1.php)

### GET VS POST방식

[GET방식예제](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/ex2.php)  
[POST방식예제1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/ex3.php)  
[POST방식예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/ex4.php)

- GET방식 : URL에 데이터를 첨부해서 전송하는 방식
- POST방식 : HTTP 메시지의 본문에 데이터를 포함해서 전송

GET 방식은 정보에 대한 링크로 많이 사용되고, POST 방식은 사용자의 아이디나 비밀번호와 같은 데이터를 전송하는 방식으로 주로 사용한다.

## 조건문

### if

가정법,뜻 : 만약에

[if예제1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/condition1.php)  
[if예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/condition2.php)  
[if예제3](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/condition3.php)  
[if예제4](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/condition4.php)  
[if예제5](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/condition5.php)  
[if예제6](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/condition6.php)

### 변수와 비교연산자 그리고 조건문

1. GET방식
   [GET방식 로그인예제1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/condition8.html)  
   [GET방식 로그인예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/condition9.php)

2. POST방식
   [POST방식 로그인예제1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/condition10.html)  
   [POST방식 로그인예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/condition11.php)

### 논리연산자

1. and (&&) : 둘다참

[and연산자 예제1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/13.html)

[and연산자 예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/14.php)

2. or (||) : 둘중 하나라도 true면 true

[or연산자 예제](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/15.php)

[and/or연산자 예제](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/16.php)

### !

부정의 의미로 boolean의 값을 역전시킨다.

```
<?php
if (!true and !true){
    echo 1;
}
if (!true and !false){
    echo 2;
}
if (!false and !true){
    echo 3;
}
if (!false and !false){
    echo 4;
}
?>
```

### boolean의 대체제

true,false여야만 boolean이 되는 건 아니다. 관습적인 이유로 0는 false 0이 아닌 숫자는 true를 대체할 수 있다.  
0외에 값이 없는 배열, 빈문자열, NULL, 문자 0 등도 0으로 간주된다.

```
<?php
//1:true , 0:false
if (1 and 1) {
    echo 1;
}
if (1 and 0) {
    echo 2;
}
if (0 and 1) {
    echo 3;
}
if (0 and 0) {
    echo 4;
}
?>
```

### 참고 (php공식사이트 문서)

http://php.net/manual/en/types.comparisons.php

## 반복문

반복문은 컴퓨터에게 반복적인 작업을 지시하는 방법이다.

### while

```
while(조건){
    코드
    코드
}
```

[while 예제1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/17.php)

[while 예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/18.php)

### for

```
<?php
while(true) {
    echo 'coding everybody';
}
?>
```

[for 예제](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/19.php)

### 반복문의 제어

[continue,break 예제](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/20.php)

### break

반복작업을 중간에 중단시키고 싶으면 break를 사용한다.

### continue

실행을 즉시 중단하면서 반복을 지속되게 한다.

### 반복문의 중첩

[반복문의 중첩 예제](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/21.php)

## 함수

한번작성한 코드를 언제나 재실행할 수 있는 코드의 재활용성을 높여준다.

```
function 함수명( [인자...[,인자]] ){
   코드
   return 반환값;
}
```

[function 예제1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/22.php)

[function 예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/23.php)

[function 예제3](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/24.php)

### 인자

인자는 함수로 유입되는 입력값을 의미한다.어떤 값을 인자로 전달하느냐에 따라서 함수가 반환하는 값이나 메소드의 동작방법을 다르게 할 수 있다.

[인자 예제1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/25.php)

값전달순서  
![](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/6/1786.png)

[인자 예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/26.php)

값전달순서  
![](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/6/1787.png)

### 인자의 기본값

기본값이란 인자의 값이 주어지지 않았을 때 사용할 값을 의미한다.

[인자 예제3](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/27.php)

## 배열

배열이란 다른 언어에서는 리스트라고도 하는 형태의 데이터 타입이다. 배열은 연관된 데이터를 모아서 관리하기 위해서 사용하는 데이터 타입이다. 변수가 하나의 데이터를 임시로 저장하기 위한 것이라면 배열은 여러 개의 데이터를 저장하기 위한 것이라고 할 수 있다.

[배열 예제1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/28.php)

[배열 예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/29.php)

[배열 예제3](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/30.php)

[배열 예제4](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/31.php)

### 배열의 사용

배열의 진가는 반복문과 결합했을 때 나타난다. 반복문으로 배열에 담긴 정보를 하나씩 꺼내서 처리 할 수 있기 때문이다.

[배열 예제5](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/32.php)

### 배열의 조작

### 추가

![](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/6/1788.png)

[추가 예제1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/33.php)

[추가 예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/34.php)

### 제거

[제거 예제1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/35.php)  
[제거 예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/36.php)

### 정렬

[제거 예제1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/37.php)  
[제거 예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/38.php)

### 연관배열

지금까지 살펴본 배열은 아이템에 대한 식별자로 숫자를 사용했다.데이터가 추가되면 배열 전체에서 중복되지 않는 인덱스가 자동으로 만들어져서 그 데이터에 대한 식별자가 되는 것이다. PHP에서는 인덱스로 문자를 사용하는 것도 가능하다. 일반적으로 다른 언어에서는 숫자를 인덱스로 사용하는 것을 일반적으로 배열, 혹은 indexed array라고 하고, 문자를 인덱스로 사용하는 것을 연관배열(associative array, hash, dictionary)라고 부르지만 PHP에서는 이를 특별히 구분하지 않고 있기 때문에 하나의 배열의 키 값으로 숫자와 문자 모두를 사용할 수 있다.

[연관배열 예제1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/39.php)

[연관배열 예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/40.php)

## include와 namespace

코드 하나가 여러개의 파일로 분리하게 됨으로써 얻을 수 있는 효과

- 자주 사용되는 코드를 별도의 파일로 만들어서 필요할 때마다 재활용할 수 있다.
- 코드를 개선하면 이를 사용하고 있는 모든 애플리케이션의 동작이 개선된다.
- 코드 수정 시에 필요한 로직을 빠르게 찾을 수 있다.
- 필요한 로직만을 로드해서 메모리의 낭비를 줄일 수 있다.

### include

include란 필요에 따라서 다른 php파일을 코드 안으로 불러와서 사용할 수 있는 것이다.

[include 예제1-1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/greeting.php)

[include 예제1-2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/41.php)
PHP는 외부의 php 파일을 로드하는 방법으로 4가지 형식을 제공한다. 형식의 종류는 아래와 같다.

- include
- include_once
- require
- require_once

include와 require의 차이점은 존재하지 않는 파일의 로드를 시도했을 때 include가 warning를 일으킨다면 require는 fatal error를 일으킨다는 점이다. fatal error는 warning 보다 심각한 에러이기 때문에 require가 include 보다 엄격한 로드 방법이라고 할 수 있다.  
`_once`라는 접미사가 붙은 것은 파일을 로드 할 때 단 한번만 로드하면 된다는 의미다.

### namespace

디렉토리를 이용하면 같은 이름의 파일이 하나의 컴퓨터에 존재할 수 있다.
네임스페이스란 간단하게 디렉토리와 같은 것이라고 생각해보자. 하나의 에플리케이션에는 다양한 모듈을 사용하게 된다. 그런데 모듈이 서로 다른 개발자에 의해서 만들어지기 때문에 같은 이름을 쓰는 경우가 생길 수 있다. 이런 경우 먼저 로드된 모듈은 나중에 로드된 모듈에 의해서 덮어쓰기 되기 때문에 이에 대한 대책이 필요하다. 네임스페이스가 필요해지게 되는 것이다.

[include 예제2-1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/greeting_en.php)  
[include 예제2-2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/greeting_ko.php)  
[include 예제2-3](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/42.php)

위의 코드는 아래와 같은 에러를 발생시킨다.

```
Fatal error: Cannot redeclare welcome() (previously declared in D:\BitNami\wampstack-5.4.12-0\apache2\htdocs\include\greeting_ko.php:3) in D:\BitNami\wampstack-5.4.12-0\apache2\htdocs\include\greeting_en.php on line 4
```

로드한 두개의 파일 모두 welcome라는 함수를 선언했기 때문이다. PHP에서는 함수의 중복 선언을 허용하지 않는다. 이런 경우 네임스페이스를 사용할 수 있다.

[include 예제3-1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/greeting_en_ns.php)  
[include 예제3-2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/greeting_ko_ns.php)  
[include 예제3-3](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/43.php)

위의 예제와 같이 네임스페이스를 사용하게 되면 동일한 이름의 함수를 하나의 php에플리케이션 안에서 사용할 수 있다.

하나의 파일에는 복수의 네임스페이스가 존재 할 수도 있다.

## UI와 API

UI는 User Interface의 약자다. 이것은 시스템과 사용자 사이의 접점을 의미하는데, 사용자의 의지를 시스템에게 전달하면서, 시스템의 상태를 사용자에게 알려주는 장치, 그래픽, 명령어들을 포괄적으로 UI라고 부른다. 다음 그림은 php의 현재 상태를 보여주는 페이지이다. 사용자가 브라우저의 주소창에 localhost/i.php라고 입력하면 서버는 이 페이지를 사용자에게 보여준다. 이 맥락에서 브라우저의 주소입력창과 php의 정보를 보여주고 있는 웹페이지가 UI라고 할 수 있다.

![](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/62/1806.png)

API는 Application Programming Interface의 약자로 (운영체제나 언어 같은) 플랫폼과 그 플랫폼 위에서 동작하는 응용 프로그램이 상호작용하는 접점이라고 할 수 있다. 말이 어렵다. 아래 코드를 실행하면 현재 설치된 php에 대한 다양한 정보를 볼 수 있다.

```
<?php
phpinfo();
?>
```

내장 함수인 phpinfo가 자체적으로 가지고 있는 기능들은 아래와 같다.

- php의 버전과 같은 정보들
- php에 설치된 확장 기능들

이 페이지는 phpinfo라는 이름의 함수로 이미 만들어져서 준비되어 있는 것이다.여러분이 이것을 사용할 때는 단지 phpinfo()를 호출하면 되는데 이 함수와 같은 것을 API라고 한다. 사용자가 UI를 이용해서 응용프로그램이 제공하는 기능을 사용하듯이 여러분은 API를 이용해서 플랫폼(여기서는 PHP엔진)이 제공하는 기능을 자신이 만들고 있는 응용 프로그램에서 사용할 수 있게 되는 것이다. phpinfo와 같은 함수를 언어에 기본적으로 내장되어 있다고 내장함수라고도 부른다.  
아래 예제는 현재 시간을 출력하는 예제다.

```
<?php
echo date('Y-n-j H:m:s');
?>
```

만약 아래와 같은 에러가 발생한다면

```
Warning: phpinfo(): It is not safe to rely on the system's timezone settings. You are *required* to use the date.timezone setting or the date_default_timezone_set() function. In case you used any of those methods and you are still getting this warning, you most likely misspelled the timezone identifier. We selected the timezone 'UTC' for now, but please set date.timezone to select your timezone. in D:\BitNami\wampstack-5.4.12-0\apache2\htdocs\library\1.php on line 2
```

php.ini 파일에서 아래의 코드를 data.timezone = UTC로 변경한 후에 웹서버를 재시작한다.
`;date.timezone =`

실행결과는 아래와 같은 형식으로 현재 시간을 출력할 것이다.  
`2020-11-7 10:11:33`
내장 함수 date를 호출함으로서 현재 시간을 알아낼 수 있었다. 자신의 응용 프로그램에서 현재 시간을 알아야 한다면 date라는 API를 사용해야 한다는 것을 알아야 한다. 응용 프로그램의 개발자에게 응용 프로그램의 플랫폼이 제공하는 API를 폭넓고 깊게 이해하는 것은 매우 중요하다.

### PHP의 표준 라이브러리 문서

PHP는 웹개발에 필요할만한 수 많은 내장함수를 제공한다. 이 내장함수들은 빠르게 웹에플리케이션을 구축하는데 도움을 주고, 직접 구현하는 것보다 실행속도가 빠르기 때문에 어떤 기능을 구현하기에 앞서서 API가 있는지 찾아보는 것이 바람직하다.  
http://us1.php.net/manual/en/

## composer

컴포저는 PHP의 의존성 관리도구이다. 필요한 확장 기능을 쉽게 설치해주는 기능도 제공하지만, 프로젝트에서 필요한 확장 기능을 통합해서 관리해주는 도구다.

### packagist

packagist는 컴포저의 메인 저장소이다.
https://packagist.org/

### composer 설치법

1. window 자동설치를 통해 composer파일을 php설치경로에 저장한다.

2. composer.phar설치파일이 생성된 것을 확인하고나서 cmd실행

3. https://getcomposer.org/doc/00-intro.md 사이트의 'echo @php "%~dp0composer.phar" %\*>composer.bat' 명령어 복사

4. cmd에서 php설치경로로 이동한 다음 위의 명령어를 붙여넣어 실행한다.

5. composer명령을 쳐서 메뉴얼이 나오는지 확인, 만약에 다른 경로에서도 composer명령어를 실행하고 싶다면 php설치경로로 환경변수 path설정하면 된다.

6. packagist주소에서 markdown 검색

![](../img/img2.png)

7. 인기많고 다운로드수가 많은 곳으로 들어가서 표시된 부분의 require ~ 를 복사한다.

![](../img/img3.png)

8. 아래와 같이 해당경로에 composer.json파일 생성하여 require ~ 붙여넣는다.

![](../img/img5.png)

9. cmd에서 json파일 생성한 폴더로 이동하고 난 후에 composer install 실행한다.

![](../img/img4.png)

### composer.lock

컴포저를 인스톨하면 composer.lock 파일이 생성된다. 이 파일의 내용을 열어보면 현재 설치된 라이브러리를 이용하기 위해서 필요한 선행 라이브러리들의 항목과 정확한 버전이 기술되어 있다. 이것은 일종의 스냅샷이라고 할 수 있는데 지금 상태를 기록해둔 것이다. 컴포저 인스톨을 실행했을 때 이 파일이 존재한다면 컴포저는 이 파일에 기술된 라이브러리와 다른 버전의 라이브러리만을 설치할 것이다.  
만약 라이브러리를 최신버전으로 갱신하고 싶다면 아래와 같이 update 명령을 사용하면 된다.
`require 'vendor/autoload.php';`

## 파일

### 파일복사

[파일복사 예제](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/file/1.php)

example.txt.bak 파일생성됨

### 파일삭제

[파일삭제 예제](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/file/2.php)

### 파일 읽고쓰기

### file_get_contents

- 텍스트로 이루어진 파일을 읽어서 문자열을 리턴한다,
- http://docs.php.net/manual/kr/function.file-get-contents.php
- http://docs.php.net/manual/kr/function.fread.php
  > 좀 더 고급스러운 파일 제어를 원한다면 fopen을 참조하자.

[file_get_contents 예제1](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/file/3.php)

### 네트워크를 통해서 데이터 읽어오기

[file_get_contents 예제2](https://github.com/kjhabc2002/TIL/blob/master/php/Exam2020/file/5.php)

### file_put_contents

- 문자열을 파일에 저장한다.
- http://docs.php.net/manual/kr/function.file-put-contents.php
- http://docs.php.net/manual/kr/function.fwrite.php
