<?php
	$attributes_course = $_GET["attributes_course"];
	$attributes_cuisine = $_GET["attributes_cuisine"];
	$attributes_holiday = $_GET["attributes_holiday"];
	$flavours_salty = $_GET["flavours_salty"];
	$flavours_sour = $_GET["flavours_sour"];
	$flavours_sweet = $_GET["flavours_sweet"];
	$flavours_bitter = $_GET["flavours_bitter"];
	$flavours_meaty = $_GET["flavours_meaty"];
	$flavours_piquant = $_GET["flavours_piquant"];
	$rating = $_GET["rating"];
	$id = $_GET["id"];
	$smallImageUrlsToString = $_GET["smallImageUrlsToString"];
	$sourceDisplayName = $_GET["sourceDisplayName"];
	$totalTimeInSeconds = $_GET["totalTimeInSeconds"];
	$ingredientsToString = $_GET["ingredientsToString"];
	$recipeName = $_GET["recipeName"];

	if (@mysql_connect('localhost','root','panorama')) {
			if (@mysql_select_db('Database_Sandipan')) {
				
				$query = "INSERT INTO Table_Sandipan(Serial,Attributes_Course,Attributes_Cuisine,Attributes_Holiday,Flavours_Salty,Flavours_Sour,Flavours_Sweet,Flavours_Bitter,Flavours_Meaty,Flavours_Piquant,Rating,ID,Small_Image_Url,Source_Display_Name,Total_Time_In_Seconds,Ingredients,Recipe_Name) VALUES (null,'".$attributes_course."','".$attributes_cuisine."','".$attributes_holiday."','".$flavours_salty."','".$flavours_sour."','".$flavours_sweet."','".$flavours_bitter."','".$flavours_meaty."','".$flavours_piquant."','".$rating."','".$id."','".$smallImageUrlsToString."','".$sourceDisplayName."','".$totalTimeInSeconds."','".$ingredientsToString."','".$recipeName."')";
				mysql_query($query);
				}

			}

?>
