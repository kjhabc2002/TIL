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

[script방식예제3 | 잘못된 방식](https://github.com/kjhabc2002/TIL/blob/master/javascript/load/script3.html)

script를 head태그에 위치시킬 수 있다. 하지만 이 경우는 오류가 발생한다.

[script방식예제3 | 올바른 방식](https://github.com/kjhabc2002/TIL/blob/master/javascript/load/script3-1html)

window.onload = function(){} 함수는 웹브라우저의 모든 구성요소에 대한 로드가 끝났을 때 브라우저에 의해서 호출되는 함수다. 이러한 것을 이벤트라고 하는데 이벤트는 뒤에서 배울 것이다.

## Object Model
