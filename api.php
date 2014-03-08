<?php

    ini_set("display_errors", 1);
    
    $url=$_SERVER['REQUEST_URI'];  
       
    
    $data["name"] = "Victor";
    $data["content"] = "prueba";
   
    echo json_encode($data);
    
    //echo json_encode($url);
    
    
    //echo $_GET['callback']."(".json_encode($arr).");";
?>