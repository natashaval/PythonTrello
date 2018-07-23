<?php
//https://stackoverflow.com/questions/24533938/class-mongoclient-not-found

require 'vendor/autoload.php';

$data = file_get_contents('php://input');
$events = json_decode($data);
$array = json_decode($data,true);

print_r($array);

 $model_id = $array['model']['id'];

 //ganti counternya
 $counter = 10;
 $parameter = "python script/Mongo_ScaleOrganization.py $model_id $counter";
 print_r($parameter);
 $output = shell_exec($parameter);
 var_dump($output);
?>
