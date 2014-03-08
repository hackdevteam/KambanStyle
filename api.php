<?php

    ini_set("display_errors", 1);
    
    $url=$_SERVER['REQUEST_URI'];

   
   
    
    /*$values = split("/", $url);
      
    foreach ($values as $value){
        if ($value != "" ){
            echo $value;
        }
    }*/
       
   
    $arr["name"] = "Victor";    
    $arr["content"] = "Probando probando";
    
    json_econde($arr);
    
    //echo json_encode($url);
    
    
    //echo $_GET['callback']."(".json_encode($arr).");";
?>