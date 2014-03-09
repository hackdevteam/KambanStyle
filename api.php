<?php

    ini_set("display_errors", 1);
    
    $url=$_SERVER['REQUEST_URI'];

     
    
    $data["name"] = "Victor";
    $data["content"] = "prueba afasdfasd";
   
    echo json_encode($data);
?>