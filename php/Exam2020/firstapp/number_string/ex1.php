<html>
<body>
<?php
//$_GET['id']는 url의 내용 중에서 ?id=  뒤에 따라오는 데이터로 치환
//id값,password값을 출력
//입력 : http://localhost:81/firstapp/number_string/ex1.php?id=kjh&password=11111
//출력 : kjh,11111
echo $_GET['id'].','.$_GET['password'];
?>
</body>
</html>
