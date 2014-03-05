<?php

    ini_set("display_errors", 1);
    
    $url=$_SERVER['REQUEST_URI'];

   
   
    
    /*$values = split("/", $url);
      
    foreach ($values as $value){
        if ($value != "" ){
            echo $value;
        }
    }*/
       
   
    $arr["body"] = json_decode($_POST['valor']);
    
    
    echo $_GET['callback']."(".json_encode($arr).");";
?>