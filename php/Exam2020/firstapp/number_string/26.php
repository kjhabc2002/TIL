<?php
function get_arguments($arg1, $arg2){   #인자가 arg1,arg2 두개다.
  return $arg1 + $arg2;          #지역변수 : 선언된 함수 안쪽에서만 사용할 수 있는 변수
}
echo get_arguments(10,20);       #30
echo get_arguments(20,30);       #50

 ?>
