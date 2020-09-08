<html>
<body>
<?php
for($i=0;$i<10;$i++){
  if($i===5){
    //break;           //변수i가 5가되면서 반복문 종료
    continue;          //i의 값이 5가 되었을 때 실행이 중단 됐기 때문에 continue 이후의 구문이 실행되지 않음
                      //하지만 반복문은 중단되지 않았기 때문에 나머지 결과가 출력된 것이다.
  }
  echo "coding everybody{$i}<br  />";
}
 ?>
</body>
</html>
