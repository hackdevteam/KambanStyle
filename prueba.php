<?php

    $url=$_SERVER['REQUEST_URI'];

   
    $arr['#cb'] = $url;
      

    
    
    echo $_GET['callback']."(".json_encode($arr).");";
?>