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
