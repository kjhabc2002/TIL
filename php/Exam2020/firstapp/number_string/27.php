<?php
function get_arguments($arg1=100){  #기본값=100
  return $arg1;
}
echo get_arguments(1);    #1
echo ',';
echo get_arguments();     #인자의 값이 아무것도 없다면 정의된 arg1인자의 값에 의해 100이 된다.
 ?>
