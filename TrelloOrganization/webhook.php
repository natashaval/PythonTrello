<?php
	$data = file_get_contents('php://input');
	$events = json_decode($data,true);
	$board_id = $events['model']['id'];
	//$counter;

if (!empty($events)){
	// get counter saat ini dari mongoDB
	$cmd_counter = "python Mongo_GetCounter.py $board_id";
	$string_counter = shell_exec($cmd_counter);
	
	$counter = (int)$string_counter;
	print_r($board_id);
	var_dump($string_counter);
	var_dump($counter);
	// hasil output berbentuk string =/= HARUS int agar bisa diincrement

	++$counter;
//	if ($counter >= 5){
		$cmd_update_board = "python Mongo_ScaleOrganization.py $board_id $counter";
		$output = shell_exec($cmd_update_board);
		var_dump($output);
//	}
}
else {
	//echo "Ini hasil counter: $counter";
}

?>