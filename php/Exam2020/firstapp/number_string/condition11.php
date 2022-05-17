<?php
if($_POST['id']==='egoing'){
  if($_POST['password'] === '11111'){       //조건문 중첩
    echo 'right';
  }else{
    echo 'password wrong';
  }
}else {
  echo "id wrong";
}
 ?>
