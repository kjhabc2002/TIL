# CSS 수업

CSS는 HTML을 아름답게 꾸며주는 디자이너의 언어입니다.

시간이지날수록 사람들은 웹페이지가 더 아름다워지기를 바랬다.
그러면서 html에는 정보+디자인으로 디자인을 동시에 갖기 시작했다.

네가지 질문에 대답할 수 있다면 완벽이해 🥕

1. CSS는 어떤 목적의 언어인가요?
2. CSS를 웹페이지에 삽입하는 방법은 무엇인가요?
3. style속성은 무엇인가요?
4. 선택자는 무엇인가요?

---

1. 답 : css는 html웹페이지를 더 아름답게 만들어주는 언어입니다.
2. 답 : link태그를 이용하여 css파일을 불러온다.
3. 답 : style속성은 마치 script태그처럼 웹브라우저에게 style속성에 감싸져있는 것들을 알려주는 역할을 하는 구분자입니다.
4. 답 : 선택자는 말그대로 선택을 해주는 요소입니다. 이를 통해 특정 요소들을 선택하여 스타일을 적용할 수 있게 됩니다.

---

## 1. 선택자

### 1.1 선택자와 선언

[선택자예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/selector_decoration_1.html)
어떤 태그를 디자인하기 위해서는 디자인하려는 태그를

1. 선택하고(선택자) (주어)
2. 선택한 대상에게 효과를 줘야 합니다.(선언) (서술어)

![](https://media.vlpt.us/images/rimu/post/cd5153b9-9e40-4467-8f75-c17d2e188ee4/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-04-20%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.36.20.png)

### 1.2 선택자의 종류

선택자의 타입들

- 태그 선택자
- 클래스 선택자
- 아이디 선택자

### 1.2.1 태그선택자

[태그선택자예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/selector_decoration_1.html)
태그를 선택합니다. 아래코드는 이 문서의 모든 li태그라는 것입니다.
li{color:red}

### 1.2.2 아이디 선택자 (학번1명 #)

[아이디선택자예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/selectors_1.html)
아이디 속성의 값에 해당하는 태그를 선택하는 선택자입니다. 아래의 코드는 이 문서에서 id값이 select인 태그라는 뜻입니다.
#select{font-color:50px;}

### 1.2.3 클래스 선택자 (반전체 .)

[클래스선택자예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/selectors_2.html)
클래스 속성의 값에 해당하는 태그들을 선택하는 선택자입니다.

### 1.3 부모 자식 선택자

[부모자식 선택자예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/template.html)

### 1.3.1 조상 자손 선택자

아래의 태그는 ul 밑에 있는 모든 태그를 선택합니다.

```
ul li{
    color:red;
}
```

### 1.3.2 부모 자식 선태

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

### 1.3.3 선택자 공부 팁

선택자를 쉽게 공부하고 찾아 쓸 수 있는 방법
[링크참고 | css selectors cheatsheat](https://frontend30.com/css-selectors-cheatsheet/)

### 1.4 가상 클래스 선택자

[가상 클래스 선택자예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/psuedo.html)
가상 클래스 선택자는 클래스 선택자처럼 행동하지만 클래스 선택자가 아닌 선택자(엘리먼트의 특성에 따라 클래스 선택자처럼 몇몇 태그를 그룹핑한다.)

### 1.4.1 링크와 관련된 가상 클래스 선택자

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

### 1.5 여러가지 선택자들

[링크참고](http://flukeout.github.io/)

---

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
http://www.w3schools.com/css/css_colors.asp

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

### 2.4.1 font-weight (폰트의 두께)

bold사용

### 2.4.2 line-height (행과 행사이의 간격)

기본값은 normal로 수치로는 1.2에 해당합니다.
이 수치를 기준으로 간격을 조정하면 됩니다.
값이 1.2라면 현재 엘리먼트 폰트 크기의 1.2배만큼 간격을 준다는 의미입니다.

### 2.4.3 font

폰트와 관련된 여러 속성을 축약형으로 표현하는 속성입니다.
형식은 아래와 같습니다.(순서지켜야함)

font: font-style font-variant font-weight font-size/line-height font-family|caption|icon|menu|message-box|small-caption|status-bar|initial|inherit;

### 2.4.4 서체

[고정폭과 가변폭 | 생활코딩 참고](https://opentutorials.org/module/2367/13362)

### 2.4.5 웹폰트

[font-family예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/font-family.html)

---

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

---

## 4. 레이아웃 ⭐️⭐️

구획을 나누고 적절히 정보를 배치하는 것을 레이아웃(layout)이라고 합니다.

### 4.1 인라인 vs 블럭레벨

[inline-block예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/inline-block.html)

html엘리먼트들은 크게 두가지로 구분됩니다.

- 화면 전체를 사용하는 태그 => block element
- 화면의 일부를 차지하는 태그 => inline level element

display속성을 이용하면 블록 레벨 엘리먼트를 인라인 엘리먼트로, 인라인 레벨 엘리먼트를 블록 레벨 엘리먼트로 바꿀 수 있다.

### 4.2 박스모델

[box예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/box.html)

박스모델은 각 태그들이 웹페이지에 표현될때 사각형의 형태(box)로 그 태그의 부피감을 결정한다.

박스모델 관련 속성들 : width, height, margin, padding, display, border ...

- margin : 태그와 태그 사이의 여백
- padding : 태그와 내부 컨텐츠 사이의 여백
- border : width style color; 순서로 값 지정

* inline element는 width, height값이 무시된다.

### 4.3 box-sizing

[box-sizing예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/box-sizing.html)

box-sizing은 박스의 크기를 화면에 표시하는 방식을 변경하는 속성입니다.  
width와 height는 엘리먼트의 컨텐츠의 크기를 지정합니다.
따라서 테두리가 있는 경우에는 테두리의 두께로 인해서 원하는 크기를 찾기가 어렵습니다.  
box-sizing속성을 border-box로 지정하면 테두리를 포함한 크기를 지정할 수 있기 때문에 예측하기가 더 쉽습니다. 최근엔 모든 엘리먼트에 이 값을 지정하는 경우가 늘고 있습니다.

### 4.4 마진겹침 현상 🌟🌟🌟

마진겸침(margin-collapsing)현상은 상하 마진값이 어떤 상황에서 사라지는 현상을 의미합니다.

- 위, 아래 엘리먼트들의 마진이 겹칠 시 둘 중 마진이 큰게 둘 사이의 마진이 된다.  
   [마진겹침 현상예제1](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/margin_collapsing_1.html)
- 위, 아래 엘리먼트들의 마진이 겹치고, 한 엘리먼트의 시각적 요소가 없어지면, 시각적 요소가 없어진 엘리먼트 마진의 top-bottom과 left-right은 큰값으로 합쳐져 계산된다.  
   [마진겹침 현상예제2](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/margin_collapsing_2.html)  
   3.부모,자식 엘리먼트 사이에서 부모의 시각적 요소가 없어지면 부모,자식 중 마진이 큰 쪽이 자식 마진처럼 사용된다.  
   [마진겹침 현상예제3](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/margin_collapsing_3.html)

### 4.5 포지션 😫

엘리먼트의 위치를 지정하는 4가지 방법이 있습니다.

- static
- relative
- absolute
- fixed

### 4.5.1 static vs relative

[position예제1](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/position_1.html)

position속성 미지정시 기본값은 static  
static : 원래 있어야 되는 위치에 정적으로 위치함(offset무시)  
 위치 설정이 되지 않은 상태 (이동없이 생성된 위치를 고수)

top,bottom,left,right(offset)을 적용하고 싶을 경우 position의 값을 static외의 값으로 지정해야 한다.(bottom,right < top,left 적용)

\*poisition을 지정해도 offset값을 지정하지 않을 경우 static처럼 원래 있어야 할 위치에 있게된다.

relative : 원래 위치에서 상태적으로 위치를 변경

### 4.5.2 absolute

[position예제2](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/position_2.html)

absolute : html element를 기준으로 절대적인 위치로 변경

부모-자식 관계에 놓인 태그의 경우

1. 자식 태그가 absolute일 경우 부모태그는 자신의 크기만 가진다.
   이때, 자식 태그는 block태그여도 inline태그처럼 컨텐츠만한 크기로 변한다.
   width와 height 값을 지정하면 크기 변경이 가능하다. (fixed여도 같은 효과)

2. 여러 부모태그 중 absolute인 자식태그는 position이 relative인 부모태그 안에서 절대적으로 위치를 변경한다.

### 4.5.3 fixed

[position예제3](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/position_3.html)  
화면의 위치에 고정시켜 스크롤으로부터 독립되게 한다.  
absolute와 같이 부모 element와 독립되기 때문에 width와 height값을 다시 입력해주어야 한다.

### 4.6 flex 🌟🌟🌟🌟

css의 flex는 엘리먼트들의 크기나 위치를 쉽게 잡아주는 도구입니다.

### 4.6.1 flex의 기본

[flex예제1](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/flex_1.html)

flex를 사용하기 위해서는 컨테이너 태그에 display:flex 속성을 부여해야 합니다. 또한 flex-direction을 이용해서 정렬방향을 바꿀 수 있습니다. 기본은 row입니다.

### 4.6.2 grow & shrink

[flex예제2](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/flex_2_grow_shrink.html)
아이템은 컨테이너의 크기에 따라서 작아지기도 하고 커지기도 합니다. 이때 작아지고 커지는 비율을 지정하는 방법이 바로 grow & shrink 입니다.

### 4.6.3 Holy Grail layout

[flex예제3](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/flex_3_holygrailLayout.html)  
Holy Grail은 성배라는 뜻입니다. 많은 사람들이 성배를 찾기 위해서 노력했지만 찾지 못한 것처럼 많은 사람들이 아래와 같은 레이아웃을 만들기 위해 노력했지만 완벽한 방법을 찾지 못했습니다. 이것에 비유해서 이런 레이아웃을 성배 레이아웃이라고 부르곤 했습니다. flex는 아주 세련된 방법으로 이 문제를 간편하게 해결합니다. 여기서는 플렉스를 이용해서 성배 레이아웃을 만드는 법을 알아봅시다.

![](https://s3-ap-northeast-2.amazonaws.com/opentutorials-user-file/module/2367/4744.png)

### 4.6.4 flex의 여러 속성들

[flex예제3](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/flex_3_holygrailLayout.html)

기타속성 참고사이트 : https://codepen.io/enxaneta/pen/adLPwv

### 4.7 media query

[미디어쿼리예제1](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/mediaquery.html)  
[미디어쿼리예제2](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/mediaquery_2.html)  
media query는 화면의 종류와 크기에 따라서 디자인을 달리 줄 수 있는 css기능입니다.

### 4.8 float

float는 편집 디자인에서 이미지를 삽화로 삽입할 때 사용하는 기법입니다. 또한 레이아웃을 잡을 때도 사용하는 기능이기 때문에 꽤 중요합니다.

[float예제1](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/float.html)

### 4.8.1 float를 활용한 holy grail layout

[holy grail layout예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/float_2_holy_grail_layout.html)

### 4.9 다단(multi column)

[다단예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/multi_column.html)

다단(multi column)은 아래 신문처럼 화면을 분할해서 좀 더 읽기 쉽도록 만든 레이아웃을 의미합니다. css에서는 이러한 레이아웃을 쉽게 구현할 수 있는 기능을 제공합니다.
![](https://s3-ap-northeast-2.amazonaws.com/opentutorials-user-file/module/2367/4800.gif)

- column-count : 컬럼을 몇개로 나눌지
- column-width : 하나의 컬럼의 크기를 몇으로 할지 \*이 둘은 독립, 조합 가능
- gap : 컬럼 사이 간격
- rule-style : 컬럼 사이 선 스타일
- rule-width : 컬럼 사이 선 두께
- rule-color : 컬럼 사이 선 색깔
- column-span : 특정 태그가 컬럼을 초월하게 하고 싶을 때 all을 주면됨 (특정 태그에 사용)

참고

- [핀터레스트 스타일 레이아웃 만들기](https://opentutorials.org/module/2398/13712)
- [현재 사용해도 되는지에 대한 통계 보기](https://caniuse.com/#feat=multicolumn)

---

## 5. 그래픽

### 5.1 배경(background)

background : 엘리먼트의 배경에 이미지나 색깔 등을 지정할 수 있는 속성

- background-color : 색깔 지정
- image : 이미지 지정(배경이 투명한 이미지를 쓰면 color와 같이 쓸 수 있음)
- repeat : 반복에 관한 설정
- attachment : 스크롤 내릴 때 배경도 같이 내릴지 안내릴지
- size : 크기에 관한 설정(cover, contain : 손실있어도 꽉차게, 꽉차도 손실없게)
- position : 위치결정

### 5.2 필터(filter)

[필터예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/filter.html)

필터는 기존에 포토샵 등을 통해서 이미지나 텍스트에 필터효과를 주었던 것을 코드화한 기능

- 비교적 신기술이기 때문에 접두사를 붙이는 것이 좋다(-webket:크롬용, -o:오페라용)

[CSS filter playground](https://bennettfeely.com/image-effects/)  
[CSS-TRICKS-filter](https://css-tricks.com/almanac/properties/f/filter/)

codepen.io 사이트 참고

### 5.3 혼합(blend)

blend는 이미지와 이미지를 혼합해서 새로운 이미지를 만들어내는 기법입니다.

### 5.3.1 background-blend-mode

[혼합예제1](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/blend_1.html)  
배경과 배경(이미지,색깔 등)을 혼합
\*rpga(a는 투명도 0)

### 5.3.2 mix-blend-mode

[혼합예제2](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/blend_2.html)  
컨텐트와 배경 사이의 블랜드 효과

### 5.4 변형(transform)

transform은 엘리먼트의 크기,위치,모양을 변경하는 속성입니다.

형식

```
/* Keyword values */
transform: none;

/* Function values */
transform: matrix(1.0, 2.0, 3.0, 4.0, 5.0, 6.0);
transform: translate(12px, 50%);
transform: translateX(2em);
transform: translateY(3in);
transform: scale(2, 0.5);
transform: scaleX(2);
transform: scaleY(0.5);
transform: rotate(0.5turn);
transform: skew(30deg, 20deg);
transform: skewX(30deg);
transform: skewY(1.07rad);
transform: matrix3d(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0);
transform: translate3d(12px, 50%, 3em);
transform: translateZ(2px);
transform: scale3d(2.5, 1.2, 0.3);
transform: scaleZ(0.3);
transform: rotate3d(1, 2.0, 3.0, 10deg);
transform: rotateX(10deg);
transform: rotateY(10deg);
transform: rotateZ(10deg);
transform: perspective(17px);

/* Multiple function values */
transform: translateX(10px) rotate(10deg) translateY(5px);

/* Global values */
transform: inherit;
transform: initial;
transform: unset;
```

[변형예제1](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/transform_1.html)

[변형예제2](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/transform_2.html)

참고

- [Caniuse | 트랜스폼을 현재 얼마나 많은 브라우저가 지원하고 있는지](https://caniuse.com/#search=transform)
- [mdn transform](https://developer.mozilla.org/en-US/docs/Web/CSS/transform)
- [hover.css](http://ianlunn.github.io/Hover/)
- [CSShake](http://elrumordelaluz.github.io/csshake/#1)
- [magic animation](https://www.minimamente.com/project/magic/)

### 5.5 SVG

svg는 백터(vector) 이미지를 표현하기 위한 포맷으로 w3c에서 만든 백터 이미지 표준입니다. SVG자체는 CSS가 아닙니다만 CSS를 이용해서 다양한 효과를 줄 때 SVG를 활용하는 경우가 많기 때문에 여기서는 SVG에 대해서 간략하게 언급만 하겠습니다.

[svg예제1](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/svg_1.html)  
[svg예제1](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/svg_1.html)

참고

- [svg tutorial](http://tutorials.jenkov.com/svg/index.html)
- [svg codepen](https://codepen.io/search/pens?q=svg&limit=all&type=type-pens)

---

## 6. 모션그래픽

css의 최신버전에서는 포토샵이나 플래쉬와 같은 프로그램으로 해야 했던 일을 css로도 할 수 있게 되었습니다.

### 6.1 전환(transition)

전환은 효과가 변경되었을 때 부드럽게 처리해주는 css기능입니다.

속성

- transition-duration : 몇초에 걸쳐 전환할 것인지
- transition-property : 어떤 속성에 transition을 적용할 것인지(all or 특정속성(transform,font-size 등)
- transition :위의 두 개의 속성의 축약형(transform 1s, font-size 2s 이렇게 두개 나눠서 적용가능)
- transition-delay : 처음에 시간차를 두고 전환
- transition-timing-function : 장면전환속도를 균일하지 않게(ceaser사이트 참고)

[transition예제1](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/transition_1.html)

[transition예제2](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/transition_2.html)

### 6.2 전환의 심화내용

참고

- [transition timming function 만들기](https://matthewlein.com/tools/ceaser)
- transition을 사용할 수 있는지 확인(caniuse.com)

---

## 7. 유지보수 😵

유지하고 보수하는 것이 편리하지 못하면 디자인을 과감하게 전개하는 것은 어려운 일입니다. 따라서 일정한 규모의 사이트가 되면 유지보수를 효율적으로 해서 프로젝트의 복잡도를 낮추는 것은 중요한 일이 됩니다. 여기서는 대규모의 css시스템을 구축할 때 필요한 여러가지 테크닉들을 알아봅니다.

### 7.1 link와 import

똑같은 css를 적용해야 하는 웹페이지가 1000개가 있을 때 css의 내용이 바뀌었다면 어떻게 해야할가요? 아마 천개의 웹페이지를 모두 수정해야 할 것입니다. 이것은 css의 수정을 소극적으로 만들고 그것은 곧 아름다움을 억압하는 암담한 장애물이 될 것입니다. 여기서는 이런 문제를 근본적으로 해결할 수 있는 방법인 link태그와 @import에 대해서 알아봅니다.

외부로 파일을 빼는 방법은 크게 두가지 입니다.

1. 별도의 css파일을 여러 html에 로드할 때 쓰임 (보편적임)

```
<link rel="stylesheet" href="style.css">
```

2. 링크라는 태그로 인해 html을 태그로 로드할때 쓰임, style.css파일안에서도 적용가능

```
 <style>@import url("style.css")</style>
```

[link예제1](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/link_1.html)  
[link예제2](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/link_2.html)

### 7.2 코드 경량화(minify)

CSS는 네트워크를 통해서 전송됩니다. 자연스럽게 CSS의 크기가 커지면 컨텐츠의 생산자와 소비자 모두에게 손해입니다. 코드의 크기를 줄이는 것을 통해서 이런 문제를 완화해주는 도구가 minify도구입니다.

코드의 크기가 크면 데이터를 주고받는 속도가 느리고 그것은 곧 시간이며, 돈이 되게된다.

- http://adamburgess.github.io/clean-css-online/
- [clen-css]
- [nodejs설치]

[minify예제](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/minify.html)

### 7.3 CSS 뛰어넘기(preprocessor)

CSS는 뛰어난 언어입니다. 하지만 CSS가 모든 면에서 좋을 수는 없습니다. 그래서 어떤 이들은 CSS에 편리한 기능을 더한 새로운 언어를 만들고 이 언어에 따라서 작성한 코드를 어떤 프로그램으로 실행시키면 결과적으로 CSS를 만들어주는 도구들을 개발했는데요. 이런 도구를 preprocessor이라고 합니다.

대표적인 preprocessor들입니다.

- http://lesscss.org/ (온라인 변환기)
- http://sass-lang.com/
- http://stylus-lang.com/ (온라인 변환기)

아래는 이런 도구들에 대해서 비교한 사이트입니다.

- https://csspre.com/compile/

### 7.3.1 preprocessor란?

표준화된 css문법은 아니지만 더 편리하게 개인이 커스터마이징한 기능들을 쓸 수 있고 그것을 css표준문법으로 변환해주는 기술

### 7.3.2 에디터의 확장 기능을 이용해 컴파일

1. backet에서 stylus도구 설치
2. https://github.com/phoenix3008/stylus-autocompile stylus추가정보에서
   // out: ../dist/app.css, compress: true, sourcemap: true 복사

3. pp.styl 파일에서 붙여넣기하여 활용

[preprocessor예제 | html파일](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/pp.html)

[preprocessor예제 | styl파일](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/pp.styl)

[preprocessor예제 | css파일](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/pp.css)

### 7.3.3 명령어를 이용해서 컴파일

1. https://stylus-lang.com/ -> stylus홈페이지 접속
2. \$ npm install stylus -g -> cmd터미널에 명령어 입력하여 설치
3. stylus github에서 사용법 보기  
   stylus -w style.styl -o style.css -> style.styl파일을 수정하면 컴퓨터가 감지하여 자동으로 style.css파일로 컴파일함

### 7.3.4 Stylus 문법 😱

---

## 8. library

### 8.1 fontello

팅벳폰트는 폰트 대신 어떤 문자에 해당하는 이미지로 이루어진 폰트입니다. fontello는 딩벳이나 아이콘폰트로 제공하는 여러 서비스를 모아둔 서비스입니다. 특히 svg파일을 업로드하면 폰트로 만들어주기도 합니다.

참고사이트 : <fontello.com>

- 폰트제목 옆에 🏠아이콘 누르면 폰트공급자의 홈페이지로 갈수 있다.

[fontello예제1](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/fontello_1.html)

- css는 어떠한 정보를 꾸며주는 것 뿐만아니라 시각적으로 글자를 변형시키는 것도 가능하다

[fontello예제2](https://github.com/kjhabc2002/TIL/blob/master/css3/Exam2020/fontello_2.html)

### 8.2 buttons

### 8.3 semantic-UI
