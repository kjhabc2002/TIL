<?php
//file_get_contents는 파일을 불러오는 것 뿐만아니라 불러오고 싶은 url으로도 이동이 가능하다
$homepage=file_get_contents('http://php.net/manual/en/function.file-get-contents.php');
echo $homepage;

 ?>
