<?php
$grades=array('egoing'=>10,'k8805'=>6,'sorialgi'=>80);
// grade가 한번 실행할때마다 key값과 value값 반복실행
//foreach 문은 $grades 위치의 배열에 담긴 요소의 숫자만큼 반복문을 실행한다.
//반복문이 실행될 때마다 요소의 키값을 $key 자리의 변수에 요소의 값을 $value 자리의 변수에 할당해서 반복문 안에서 접근 할 수 있도록 한다.
foreach($grades as $key=>$value){
  echo "key : {$key} value:{$value}<br  />";
}
 ?>

 <!--결과
 key : sorialgi  value : 80
 key : k8805     value : 6
 key : egoing    value : 10 -->
