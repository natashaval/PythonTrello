<?php

/* save to file 
https://stackoverflow.com/questions/21012319/how-to-increment-an-integer-and-save-it-for-future-use-without-database
*/
$filename = 'counter.txt';
$data = file_get_contents('php://input');
$events = json_decode($data,true);

if(!file_exists($filename)){
	$counter = 0;
	file_put_contents($filename, $counter);
	echo "file not exists!";
}
else if (!empty($events)){
	$counter = file_get_contents($filename);
	++$counter;
	file_put_contents($filename, $counter);
	echo "COUNTER saat ini: $counter";

	if ($counter == 49){
		$output = shell_exec("python script/MONGO_BoardTalentPool.py");
		var_dump($output);
	}
}
else {
	$counter = file_get_contents($filename);
	echo "ini hasil dari file: $counter";
}


//session_start();
//	$cookie_name = "counterWebhook";
//	global $counter;
//	setcookie($cookie_name, $counter, time() + (86400), "/");

/* cookies 2
	

	$cookie_name = "counter";
if(!isset($_COOKIE[$cookie_name])) {
    echo "Cookie named '" . $cookie_name . "' is not set!";
    $counter = 0;
	setcookie($cookie_name, $counter, time() + (86400)); 
} else if (!empty($events) && isset($_COOKIE[$cookie_name]) ){
    $counter = ++$_COOKIE[$cookie_name];
    setcookie($cookie_name, $counter, time() + (86400));
	echo "Cookie '" . $cookie_name . "' adaaa isi eventnya!<br>";
    echo "Value is: " . $_COOKIE[$cookie_name];
}
else {
	echo "Mboh ini apaa";
	echo "<br>Value is: " . $_COOKIE[$cookie_name];
}
*/

/* cookies
	if(!isset($_COOKIE['counter'])){
		echo "This is the first view!";
		$cookie = 1;
		setcookie("counter", $cookie);
	}
	else if (isset($_COOKIE['counter'])){
		echo "only refresh GET!";
	}
	else if (isset($_COOKIE['counter']) && empty($events)){
		echo "empty EVENTS";
	}
	else if (isset($events) && isset($_COOKIE['counter'])){
		echo "POST maybe";
		$cookie = ++$_COOKIE['counter'];
		setcookie("counter", $cookie);

		echo "<br>Session variables" .$_SESSION['counter']. "<br>";
	}
*/
	//echo 'Jumlah yang masuk saat ini: ';
	//print_r($counter);
	//$_SESSION["counterWebhook"] = $counter;
	//echo "<br>Session variables" .$_SESSION["counterWebhook"]. "<br>";
?>

<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>

<?php
/*
if (!isset($_COOKIE[$cookie_name])) {
	echo "Cookie named '" .$cookie_name. "' is not set!";
}
else {
	echo "Cookie '" . $cookie_name . "' is set!<br>";
    echo "Value is: " . $_COOKIE[$cookie_name];
}
*/
?>

</body>
</html>