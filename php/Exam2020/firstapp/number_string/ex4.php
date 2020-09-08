<?php
//url에 전송하는 데이터를 포함하지 않아 get방식에 비해 사용자 데이터의 노출 위험성이 적다.
echo $_POST['id'].','.$_POST['password'];
 ?>
