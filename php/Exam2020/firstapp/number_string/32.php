<?php
function get_members(){
  return ['egoing','k8805','sorialgi'];
}

$member=get_members();

for($i=0;$i<count($members); $i++){       //i<3
  //ucfirst함수는 값의 첫번째문자를 대문자로 변경해줌
  echo ucfirst($members[$i].'<br  />');  //Egoing,K8805,Sorialgi
}

 ?>
