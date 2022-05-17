<?php
require_once 'greeting_ko.php'
require_once 'greeting_en.php'
echo welcome();
echo welcome();
//두파일안의 welcome함수의 중복으로 인해 오류
 ?>
