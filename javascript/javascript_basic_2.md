# Javascript 기본

# 목차

- [웹브라우저와 JavaScript](#웹브라우저와-JavaScript)
- [실습방법](#실습방법)
- [HTML에서 javascript로드하기](#HTML에서-javascript로드하기)
  - [inline](#inline)
  - [script](#script)
  - [외부파일로 분리](#외부파일로-분리)
  - [script파일의 위치](#script파일의-위치)
- [Object Model](#Object-Model)
  - [DOM(Document Object Model)](#DOM-:Document-Object-Model)
  - [BOM(Browser Object Model)](#BOM-:Browser-Object-Model)
- [BOM](#BOM)
  - [window객체](#Window객체)
  - [전역객체](#전역객체)
  - [사용자와 커뮤니케이션 하기](#사용자와-커뮤니케이션-하기)
    - [alert](#alert)
    - [confirm](#confirm)
    - [prompt](#prompt)
  - [Location객체](#Location객체)
    - [현재 윈도우의 URL알아내기](#현재-윈도우의-URL알아내기)
    - [url parsing](#url-parsing)
    - [url 변경하기](#url-변경하기)
  - [navigator 객체](#navigator-객체)
- [DOM](#DOM)
  - [제어대상을 찾기](#제어대상을-찾기)
  - [document.getElementsByTagName](#document.getElementsByTagName)
  - [document.getElementsByClassName](#document.getElementsByClassName)
  - [document.getElementById](#document.getElementById)
  - [document.querySelector](#document.querySelector)
  - [document.querySelectorAll](#document.querySelectorAll)

## 웹브라우저와 JavaScript

- Html은 웹페이지의 표준 언어이자, 정보를 담당한다.
- css는 html를 더 아름답게 꾸며주는 디자이너의 언어이다.
- Javascript는 크게는 웹브라우저,html을 프로그래밍적으로 제어(=동적제어)하는 일을 담당하는 언어이다.

## 실습방법

- 구글 크롬 개발도구(F12) 사용
- blackets 사용

## HTML에서 javascript로드하기

### inline

[inline방식예제](https://github.com/kjhabc2002/TIL/blob/master/javascript/load/inline.html)

inline방식은 태그에 직접 자바스크립트를 기술하는 방식이다.
장점은 태그에 연관된 스크립트가 분명하게 드러난다는 점이다.
하지만 정보와 제어가 섞여 있기 때문에 정보로서의 가치가 떨어진다.

### script

[script방식예제1](https://github.com/kjhabc2002/TIL/blob/master/javascript/load/script1.html)  
script태그를 만들어서 여기에 자바스크립트 코드를 삽입하는 방식이다. html태그와 js코드를 분리할 수 있다는 장점을 가지고 있다.

### 외부파일로 분리

[script방식예제2](https://github.com/kjhabc2002/TIL/blob/master/javascript/load/script2.html)

js를 별도의 파일로 분리할 수 있는데, 더욱 엄격하게 정보와 제어를 분리할 수 있다. 하나의 js파일을 여러 웹페이지에서 로드함으로서 js의 재활용성을 높일 수 있다.
캐쉬를 통해서 속도의 향상, 전송량의 경량화를 도모할 수 있다.그리고 중복을 제거함으로써 유지보수가 편리해진다.

### script파일의 위치

script를 head태그에 위치시킬 수 있다. 하지만 이 경우는 오류가 발생한다.  
[script방식예제3 | 잘못된 방식](https://github.com/kjhabc2002/TIL/blob/master/javascript/load/script3.html)

왜 에러가 발생하는 것일까?

html파일은 위에서부터 아래로 순차적으로 읽으며 실행되는데 script태그를 만나게 되면 js코드로 인식하게 되고, script.js파일을 다운로드한다.
그런 후 script.js파일을 실행시키는데 js파일에서 id값이 hw인 element를 찾게된다. 하지만 body태그까지 실행시키지 않은 상황에서 hw element는 null로 뜨게되고 이로 인해 에러가 발생하게 된다.

해결방법은 다음과 같이 window.onload = function(){} 함수를 적용하면 된다.(window.onload = function(){} 함수는 웹브라우저의 모든 구성요소에 대한 로드가 끝났을 때 브라우저에 의해서 호출되는 함수)  
[script방식예제3 | 올바른 방식](https://github.com/kjhabc2002/TIL/blob/master/javascript/load/script3-1html)

애초에 이런일을 막을 방법은 script파일을 head태그에 두는 것보다 페이지 하단에 위치시키는 방법이 더 낫다.

1. head에 삽입되는 경우

- 브라우저 렌더링에 방해가 되어 무거운 스크립트가 실행되는 경우 오랫동안 완성되지 못한 화면을 노출하게 된다.
- 문서를 초기화하거나 설정하는 가벼운 스크립트들이 자주 사용된다.
- 문서의 DOM구조가 필요한 스크립트의 경우 document.onload와 같은 로드 이벤트가 추가되어야 에러없이 작동된다.

2. body에 삽입되는 경우

- 브라우저가 렌더링이 완료된 상태에서 스크립트가 실행되기에 콘텐츠를 변경하는 스크립트의 경우 화면에 노출된 채로 변화된다.
- 대부분의 스크립트의 위치로 추천되는 위치이다.
- dom구조가 완료된 시점에 실행되기에 별다른 추가설정이 필요없다.

## Object Model

웹브라우저의 구성요소들은 하나하나가 객체화되어 있다. 자바스크립트로 이 객체를 제어해서 웹브라우저를 제어할 수 있게 된다. 이 객체들은 서로 계층적인 관계로 구조화되어 있다. BOM과 DOM은 이 구조를 구성하고 있는 가장 큰 틀의 분류라고 할 수 있다.  
![](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/904/2229.png)

### javascript core

JavaScript 언어 자체에 정의되어 있는 객체들

### DOM :Document Object Model

- 웹페이지의 내용을 제어한다. window의 프로퍼티인 document 프로퍼터에 할당된 Document 객체가 이러한 작업을 담당한다.
- document객체는 body,img 등의 태그를 제어하는데 쓰인다.

### BOM :Browser Object Model

- 웹페이지의 내용을 제외한 브라우저의 각종 요소들을 객체화시킨 것이다. 전역객체 Window의 프로퍼티에 속한 객체들이 이에 속한다.

## BOM

### Window객체

Window 객체는 모든 객체가 소속된 객체이고, 전역객체이면서, 창이나 프레임을 의미한다.

### 전역객체

- 전역객체는 window라는 객체의 메소드를 만드는 것이다.  
  -ㅇWindow 객체는 식별자 window를 통해서 얻을 수 있다. 또한 생략 가능하다.
- 전역변수와 함수는 사실 window객체의 프로퍼티와 메소드라는 것이다. 또한 모든 객체는 사실 window의 자식객체이다.

## 사용자와 커뮤니케이션 하기

html은 form을 통해서 사용자와 커뮤니케이션할 수 있는 기능을 할 수 있다. 자바스크립트에는 사용자와 정보를 주고 받을 수 있는 간편한 수단을 제공한다.

### alert

경고창이라고도 부른다. 사용자에게 정보를 제공해주거나 디버깅 등의 용도로 많이 사용한다.

### confirm

확인을 누르면 true, 취소를 누르면 false를 리턴한다.

[script방식예제3 | 올바른 방식](https://github.com/kjhabc2002/TIL/blob/master/javascript/load/confirm.html)

### prompt

사용자가 입력한 값을 받아서 자바스크립트가 얻어낼 수 있는 기술
[script방식예제3 | 올바른 방식](https://github.com/kjhabc2002/TIL/blob/master/javascript/load/prompt.html)

## Location객체

Location 객체는 문서의 주소와 관련된 객체로 Window 객체의 프로퍼티다. 이 객체를 이용해서 윈도우의 문서 URL을 변경할 수 있고, 문서의 위치와 관련해서 다양한 정보를 얻을 수 있다.

### 현재 윈도우의 URL알아내기

아래는 현재 윈도우의 문서가 위치하는 url을 알아내는 방법이다.

```
console.log(location.toString(), location.href);
```

### url parsing

location 객체는 URL을 의미에 따라서 별도의 프로퍼티로 제공하고 있다.

```
console.log(location.protocol, location.host, location.port, location.pathname, location.search, location.hash)
```

### url 변경하기

- 아래 코드는 현재문서를 http://egoing.net으로 이동한다.

```
location.href = 'http://egoing.net';
```

- 같은 방식임

```
location = 'http://egoing.net';
```

- 현재문서를 리로드하는 간편한 방법을 제공함

```
location.reload();
```

## navigator 객체

브라우저의 정보를 제공하는 객체다. 주로 호환성 문제를 위해 사용한다.

아래 명령을 통해서 이객체의 모든 프로퍼티를 열람할 수 있다.

```
console.dir(navigator);
```

- appName : 웹브라우저의 이름

- appVersion : 브라우저의 버전

- userAgent : 브라우저가 서버측으로 전송하는 user-agent http헤더의 내용

- platform : 브라우저가 동작하고 있는 운영체제에 대한 정보

## DOM

## 제어대상을 찾기

문서 내에서 객체를 찾는 방법은 document 객체의 메소드를 이용한다.

## document.getElementsByTagName

[getElementsByTagName예제](https://github.com/kjhabc2002/TIL/blob/master/javascript/load/dom_1.html)

getElementsByTagName은 인자로 전달된 태그명에 해당하는 객체들을 찾아서 그 리스트를 NodeList라는 유사 배열에 담아서 반환한다. NodeList는 배열은 아니지만 length와 배열접근연산자를 사용해서 엘리먼트를 조회할 수 있다.

## document.getElementsByClassName

[getElementsByClassName예제](https://github.com/kjhabc2002/TIL/blob/master/javascript/load/dom_2.html)

class속성 값을 기준으로 객체를 조회할 수 있다.

## document.getElementById

[document.getElementById예제](https://github.com/kjhabc2002/TIL/blob/master/javascript/load/dom_3.html)

id값을 기준으로 객체를 조회한다. 성능면에서 가장 우수하다.

## document.querySelector

[document.querySelector예제](https://github.com/kjhabc2002/TIL/blob/master/javascript/load/querySelector.html)

css 선택자의 문법을 이용해서 객체를 조회할수도 있다.

## document.querySelectorAll

querySelector과 기본적인 동작방법은 같지만 모든 객체를 조회한다는 점이 다르다.
[document.querySelectorAll예제](https://github.com/kjhabc2002/TIL/blob/master/javascript/load/querySelectorAll.html)

## jQuery
