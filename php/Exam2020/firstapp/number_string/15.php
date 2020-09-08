<?php
//or연산자 : 조건들 중 하나라도 참이면 참
if($_POST['id'] === 'egoing' or $_POST['id'] === 'k8805' or $_POST['id'] === 'sorialgi'){
    echo 'right';
} else {
    echo 'wrong';
}
?>
