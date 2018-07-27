<?php
	require 'vendor/autoload.php';
	$database_name = "DOT-Indonesia";
	$coll = (new MongoDB\Client("mongodb://127.0.0.1:27017"))->Trello->$database_name;

	$nameQuery = array('name' => 'MAGANG DOT' );
	//$nameQuery = array();
	$out = $coll->find($nameQuery);

	$board_json = array();

	foreach($out as $doc){
		$member_array = array();
		$list_array = array();
		foreach ($doc['lists'] as $list) {
			$list_array[$list['id']] = $list['name'];
		}
		foreach ($doc['members'] as $member) {
			$member_array[$member['id']] = $member['fullName'];
		}
	
	}

	// var_dump($member_array);
	// echo "<br><br>";
	// var_dump($list_array);
	// echo "<br><br>";
	
	//echo "<ol>";
	$member_json = array();
	foreach ($member_array as $member_key => $member_value) {
		$list_json = array();
		//echo "<li>$member_value</li><ul>";
		foreach ($list_array as $list_key => $list_value) {
		//	echo "<li>$list_value</li>";
			
			$pipeline = array(
				 	array(
				 		'$match' => array('name'=>'MAGANG DOT')
				 	),
				 	array(
				 		'$unwind' => '$cards'
				 	),
				 	array(
				 		'$match' => array(
				 			'$and' => array(
				 				array('cards.idMembers'=>$member_key),
				 				array('cards.idList'=>$list_key)
				 			)
				 		)
				 	),
				 	array(
				 		'$project' => array("cards" => 1)
				 	),
				 	array(
				 		'$count' => 'jumlah'
				 	)
				 );

			$out = $coll->aggregate($pipeline);
				//var_dump($out);
			
			$GLOBALS['jumlah'] = 0;
				foreach ($out as $hasiljson) {
					//var_dump($sampah['cards']['name']);
					//var_dump($sampah['jumlah']);
					//print_r($hasiljson['jumlah']);
					$jumlah = $hasiljson['jumlah'];
					//echo "<br>";

					// var_dump($hasiljson);
					// $myjson = json_encode($hasiljson);
				}
				//echo "<br><br>";
				//$jumlah_json[$list_value] = $GLOBALS['jumlah'];
				$list_json[$list_value] = $jumlah;
		}
		//array_push($list_json, $jumlah_json);

		//array_push($member_json, $list_json);
		$member_json[$member_value] = $list_json;
		// echo "<b>MEMBER: </b>";
		// var_dump($member_json);

		//echo "</ul>";
	}
	//$board_json[$doc['name']] = $member_json;
	//echo "</ol>";
//}
	//array_push($member_json, $list_json);
	//var_dump($board_json);
	var_dump($member_json);
	$fp = fopen('sampah.json','w');
	//fwrite($fp, json_encode($board_json));
	fwrite($fp, json_encode($member_json));
	fclose($fp);
?>