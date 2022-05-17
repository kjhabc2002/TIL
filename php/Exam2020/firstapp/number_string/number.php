<?php
echo var_dump(7);  //숫자의 형식을 나타냄 integer()=정수
echo var_dump(7.1); //숫자의 형식을 나타냄 float()=실수
echo var_dump(1234);  //슷자로 인식
echo var_dump("1234");  //문자로 인식
echo "hello"."world";  //독립된 문자를 결합할때 .을 사용하여 결합
//작은따옴표로 시작하면 작은따옴표로 끝나야하고 큰따옴표로 시작하면 큰따옴표로 끝나야한다.
echo '그는 "안녕하세요 라고 말했다."\'';
//escaping ""를 문자로 인식
echo "그는 \"안녕하세요 라고 말했다.\"";
?>
