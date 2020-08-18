# CSS 수업

CSS는 HTML을 아름답게 꾸며주는 디자이너의 언어입니다.

시간이지날수록 사람들은 웹페이지가 더 아름다워지기를 바랬다.
그러면서 html에는 정보+디자인으로 디자인을 동시에 갖기 시작했다.

## 1. 선택자

### 1.1 선택자와 선언

[선택자예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/selector_decoration_1.html)
어떤 태그를 디자인하기 위해서는 디자인하려는 태그를

1. 선택하고(선택자) (주어)
2. 선택한 대상에게 효과를 줘야 합니다.(선언) (서술어)

![](https://media.vlpt.us/images/rimu/post/cd5153b9-9e40-4467-8f75-c17d2e188ee4/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-04-20%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.36.20.png)

### 1.3 선택자의 종류

선택자의 타입들

- 태그 선택자
- 클래스 선택자
- 아이디 선택자

#### 1.3.1 태그선택자

[태그선택자예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/selector_decoration_1.html)
태그를 선택합니다. 아래코드는 이 문서의 모든 li태그라는 것입니다.
li{color:red}

#### 1.3.2 아이디 선택자 (학번1명 #)

[아이디선택자예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/selectors_1.html)
아이디 속성의 값에 해당하는 태그를 선택하는 선택자입니다. 아래의 코드는 이 문서에서 id값이 select인 태그라는 뜻입니다.
#select{font-color:50px;}

#### 1.3.3 클래스 선택자 (반전체 .)

[클래스선택자예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/selectors_2.html)
클래스 속성의 값에 해당하는 태그들을 선택하는 선택자입니다.

### 1.4 부모 자식 선택자

[부모자식 선택자예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/template.html)

#### 1.4.1 조상 자손 선택자

아래의 태그는 ul 밑에 있는 모든 태그를 선택합니다.

```
ul li{
    color:red;
}
```

#### 1.4.2 부모 자식 선태

아래 선택자는 #lecture 바로 밑에 있는 li만을 선택합니다.

```
#lecture>li{
    border:1px solid red;
}
```

친구선택자(이런용어는 없습니다.)
아래코드는 ul과 ol을 동시에 선택합니다

```
ul,ol{
    background-color: powderblue;
}
```

#### 1.4.3 선택자 공부 팁

선택자를 쉽게 공부하고 찾아 쓸 수 있는 방법
[링크참고 | css selectors cheatsheat](https://frontend30.com/css-selectors-cheatsheet/)

### 1.5 가상 클래스 선택자

[가상 클래스 선택자예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/psuedo.html)
가상 클래스 선택자는 클래스 선택자처럼 행동하지만 클래스 선택자가 아닌 선택자(엘리먼트의 특성에 따라 클래스 선택자처럼 몇몇 태그를 그룹핑한다.)

### 링크와 관련된 가상 클래스 선택자

- :link - 방문한 적이 없는 링크
- :visited - 방문한 적이 있는 링크
- :hover - 마우스를 롤오보 했을 때
- :active - 마우스를 클릭했을 때

위의 선택자는 순서대로 지정하는 것이 좋습니다.  
특히 visited의 경우는 보안상의 이유로 아래와 같은 속성만 사용이 가능합니다.

- color
- background-color
- border-color
- outline-color
- The color parts of the fill and stroke properties  
  \*style태그에서 위에 있는 것이 우선순위가 높다

### 1.6 여러가지 선택자들

[링크참고](http://flukeout.github.io/)

## 2.타이포그래피

### 2.1 font-size

[폰트사이즈예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/psuedo.html)
글꼴의 크기를 지정합니다. 주요단위로는 px,em,rem이 있습니다.

1. rem : html태그에 적용된 font-size의 영향을 받습니다. html태그의 폰트크기에 따라서 상대적으로 크기가 결정되기 때문에 이해하기 쉽습니다.

2. px : 모니터 상의 화소 하나의 크기에 대응하는 단위입니다. 고정된 값이기 때문에 이해하기 쉽지만, 사용자가 글꼴의 크기를 조정할 수 없기 때문에 가급적 사용을 하지 않는 것이 좋습니다.

3. em : 부모 태그의 영향을 받는 상대적인 크기입니다. 부모의 크기에 영향을 받기 때문에 파악하기가 어렵습니다. rem이 등장하면서 이 단위 역시 사용이 권장되지 않습니다.

### 2.2 color

[컬러예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/color.html)
컬러의 다양한 종류는 아래의 페이지를 참고해주세요.
[](http://www.w3schools.com/css/css_colors.asp)

### 2.3 text-align

[text-align예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/text_align.html)
text-align의 4가지 속성값

1. left : 왼쪽 정렬
2. right : 오른쪽 정렬
3. center : 가운데 정렬
4. justify : 양쪽 정렬

### 2.4 font-family

[font-family예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/font-family.html)
font-family는 서체를 지정하는 속성입니다.

마지막 폰트는 포괄적인 폰트로 지정합니다.

- serif (장식이 있는 폰트)
- sans-serif
- cursive (흘림체)
- fantasy
- monospace (고정폭)

#### 2.4.1 font-weight (폰트의 두께)

bold사용

#### 2.4.2 line-height (행과 행사이의 간격)

기본값은 normal로 수치로는 1.2에 해당합니다.
이 수치를 기준으로 간격을 조정하면 됩니다.
값이 1.2라면 현재 엘리먼트 폰트 크기의 1.2배만큼 간격을 준다는 의미입니다.

#### 2.4.3 font

폰트와 관련된 여러 속성을 축약형으로 표현하는 속성입니다.
형식은 아래와 같습니다.(순서지켜야함)

font: font-style font-variant font-weight font-size/line-height font-family|caption|icon|menu|message-box|small-caption|status-bar|initial|inherit;

#### 2.4.4 서체

[고정폭과 가변폭 | 생활코딩 참고](https://opentutorials.org/module/2367/13362)

#### 2.4.5 웹폰트

[font-family예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/font-family.html)

## 3. 조화

### 3.1 상속

[상속예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/font-family.html)  
상속은 부모 엘리먼트의 속성을 자식 엘리먼트가 물려받는 것을 의미합니다. 상속은 css에서 생산성을 높이기 위한 중요한 기능입니다.

- 일괄적으로 어떤 속성을 적용할 때 일일이 자식들에 속성을 적용하는 것보다 부모 엘리먼트 하나에 적용시키는 것이 더 효율적이다.
- 상속 되는 속성이 있고 안되는 속성이 있다.

[컬럼 상속여부 안내사이트](https://www.w3.org/TR/CSS21/propidx.html)

### 3.2 stylish

[구글 stylish 확장프로그램](https://userstyles.org/)
stylish는 웹사이트의 디자인을 사용자 마음대로 수정할 수 있는 기능입니다. 이 기능을 이용해서 주어진대로 웹페이지를 소비하는 것이 아니라 자신의 취향을 반영할 수 있습니다. 또 다른 사람이 만든 디자인을 적용해서 간편하게 사이트의 디자인을 변경할 수도 있습니다.

### 3.3 케스케이딩

[케이케이딩예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/cascading_1.html)  
CSS는 Cascading Style Sheet의 약자입니다.
Cascading은 CSS의 첫번째 글자로 등장할만큼 가장 중요한 기능입니다. Cascading을 사전에서 찾아보면 폭포라는 의미가 있습니다. 즉, 웹페이지의 디자인이 웹브라우저의 기본 디자인과 브라우저 디자인 그리고 웹페이지 저자의 디자인이 결합될 수 있다는 점에서 착안하고 있다고 할 수 있을 것 같습니다.

즉 웹브라우저, 사용자, 컨텐츠 생산자의 조화를 중요한 철학으로 삼고 있다고 생각됩니다. 여기서는 하나의 엘리먼트에 대해서 다양한 효과가 영향력을 행사하려고 할 때 우선순위를 어떻게 설정하는가에 대한 규칙인 캐스캐이딩에 대해서 알아봅니다.

- 우선순위의 순서 : 웹브라우저 < 사용자 < 저자
- css우선순위의 순서 : 태그선택자 < class선택자 < id선택자 < style속성
- css우선순위의 기준 : 가장 포괄적인 규칙, 일반적인 것 < 구체적이면서 명시적인 규칙
- "!important"라는 키워드를 넣으면 모든 것을 무시하고 우선순위가 가장 높아진다.

## 4. 레이아웃

구획을 나누고 적절히 정보를 배치하는 것을 레이아웃(layout)이라고 합니다.

### 4.1 인라인 vs 블럭레벨

[inline-block예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/inline-block.html)

html엘리먼트들은 크게 두가지로 구분됩니다.

- 화면 전체를 사용하는 태그 => block element
- 화면의 일부를 차지하는 태그 => inline level element

display속성을 이용하면 블록 레벨 엘리먼트를 인라인 엘리먼트로, 인라인 레벨 엘리먼트를 블록 레벨 엘리먼트로 바꿀 수 있다.

### 4.2 박스모델
