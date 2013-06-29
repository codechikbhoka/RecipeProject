<!DOCTYPE html>
<html>
    <head>
			<script src="jquery1.2.js"></script>

		    <script type="text/javascript">

				    function Commer(my_array)
					{
						if (my_array.length > 0) 
							{
								var output = my_array[0]
								for (var i = 1; i < my_array.length; i++) {
									output  += ","+my_array[i]
								};
							};

						return output;
					}

				    $(function() {
						
						$('#getval').on('click',function(){
							console.log("Reached")
							$.getJSON( "http://api.yummly.com/v1/api/recipes?_app_id=e07acacf&_app_key=7dd3cec0cf3eab6a0ea750890c7e4e36&maxResult=1000&start=11000&&callback=?", function( json ) {
							console.log( "JSON Data: " + json );

							var GLOBALmatches = json.matches

							for (var i = 0; i < GLOBALmatches.length -1; i++) {
								Recipe = GLOBALmatches[i];

								var attributes_course = ""
								var attributes_cuisine = ""
								var attributes_holiday = ""
								var flavours_salty = ""
								var flavours_sour = ""
								var flavours_sweet = ""
								var flavours_bitter = ""
								var flavours_meaty = ""
								var flavours_piquant = ""
								var rating = ""
								var id = ""
								var smallImageUrlsToString = ""
								var sourceDisplayName = ""
								var totalTimeInSeconds = ""
								var ingredientsToString = ""
								var recipeName = ""

								if (Recipe.attributes) {

									if (Recipe.attributes.course) {attributes_course = Commer(Recipe.attributes.course)};
									if (Recipe.attributes.cuisine) {attributes_cuisine = Commer(Recipe.attributes.cuisine)};
									if (Recipe.attributes.holiday) {attributes_holiday = Commer(Recipe.attributes.holiday)};

								};

								if (Recipe.flavours) {
									if (Recipe.flavours.salty) {flavours_salty = Recipe.flavours.salty};
									if (Recipe.flavours.sour) {flavours_sour = Recipe.flavours.sour};
									if (Recipe.flavours.sweet) {flavours_sweet = Recipe.flavours.sweet};
									if (Recipe.flavours.bitter) {flavours_bitter = Recipe.flavours.bitter};
									if (Recipe.flavours.meaty) {flavours_meaty = Recipe.flavours.meaty};
									if (Recipe.flavours.piquant) {flavours_piquant = Recipe.flavours.piquant};


								};

								if (Recipe.rating) {rating = Recipe.rating};

								if (Recipe.id) {id = Recipe.id};

								if (Recipe.smallImageUrls) {smallImageUrlsToString = Commer(Recipe.smallImageUrls)};

								if (Recipe.sourceDisplayName) {sourceDisplayName = Recipe.sourceDisplayName};

								if (Recipe.totalTimeInSeconds) {totalTimeInSeconds = Recipe.totalTimeInSeconds};

								if (Recipe.ingredients) {ingredientsToString = Commer(Recipe.ingredients)};

								if (Recipe.recipeName) {recipeName = Recipe.recipeName};


								// var output = ""
								// output =	output.concat("attributes_course is ",attributes_course,'\n',
								// 							"attributes_cuisine is ",attributes_cuisine,'\n',
								// 							"attributes_holiday is ",attributes_holiday,'\n',
								// 							"flavours_salty is ",flavours_salty,'\n',
								// 							"flavours_sour is ",flavours_sour,'\n',
								// 							"flavours_sweet is ",flavours_sweet,'\n',
								// 							"flavours_bitter is ",flavours_bitter,'\n',
								// 							"flavours_meaty is ",flavours_meaty,'\n',
								// 							"flavours_piquant is ",flavours_piquant,'\n',
								// 							"rating is ",rating,'\n',
								// 							"id is ",id,'\n',
								// 							"smallImageUrlsToString isingredientsToString ",smallImageUrlsToString,'\n',
								// 							"sourceDisplayNamrecipeNamee is ",sourceDisplayName,'\n',
								// 							"totalTimeInSeconds is ",totalTimeInSeconds,'\n',
								// 							"ingredientsToString is ",ingredientsToString,'\n',
								// 							"recipeName is ",recipeName)

								document.getElementById("i1").value =  attributes_course
								document.getElementById("i2").value =  attributes_cuisine
								document.getElementById("i3").value =  attributes_holiday
								document.getElementById("i4").value =  flavours_salty
								document.getElementById("i5").value =  flavours_sour
								document.getElementById("i6").value =  flavours_sweet
								document.getElementById("i7").value =  flavours_bitter
								document.getElementById("i8").value =  flavours_meaty
								document.getElementById("i9").value =  flavours_piquant
								document.getElementById("i10").value =  rating
								document.getElementById("i11").value =  id
								document.getElementById("i12").value =  smallImageUrlsToString
								document.getElementById("i13").value =  sourceDisplayName
								document.getElementById("i14").value =  totalTimeInSeconds
								document.getElementById("i15").value =  ingredientsToString
								document.getElementById("i16").value =  recipeName
								

								if (window.XMLHttpRequest) {
			                        xmlhttp = new XMLHttpRequest();
			                    }

			                    var raven = "InsertInDB.php?attributes_course=" + attributes_course +
			                    								"&attributes_cuisine=" + attributes_cuisine +
			                    								"&attributes_holiday=" + attributes_holiday +
			                    								"&flavours_salty=" + flavours_salty +
			                    								"&flavours_sour=" + flavours_sour +
			                    								"&flavours_sweet=" + flavours_sweet +
			                    								"&flavours_bitter=" + flavours_bitter +
			                    								"&flavours_meaty=" + flavours_meaty +
			                    								"&flavours_piquant=" + flavours_piquant +
			                    								"&rating=" + rating +
			                    								"&id=" + id +
			                    								"&smallImageUrlsToString=" + smallImageUrlsToString +
			                    								"&sourceDisplayName=" + sourceDisplayName +
			                    								"&totalTimeInSeconds=" + totalTimeInSeconds +
			                    								"&ingredientsToString=" + ingredientsToString +
			                    								"&recipeName=" +  recipeName

			                    // var raven = "InsertInDB.php?attributes_course=" + "a" +
			                    // 								"&attributes_cuisine=" + "b" +
			                    // 								"&attributes_holiday=" + "c" +
			                    // 								"&flavours_salty=" + "d" +
			                    // 								"&flavours_sour=" + "e" +
			                    // 								"&flavours_sweet=" + "f" +
			                    // 								"&flavours_bitter=" + "g" +
			                    // 								"&flavours_meaty=" + "h" +
			                    // 								"&flavours_piquant=" + "i" +
			                    // 								"&rating=" + "j" +
			                    // 								"&id=" + "k" +
			                    // 								"&smallImageUrlsToString=" + "l" +
			                    // 								"&sourceDisplayName=" + "m" +
			                    // 								"&totalTimeInSeconds=" + "n" +
			                    // 								"&ingredientsToString=" + "p" +
			                    // 								"&recipeName=" +  "q"
			                    xmlhttp.onreadystatechange=function()
								  {
								  if (xmlhttp.readyState==4 && xmlhttp.status==200)
								    {
								    document.getElementById("display").innerHTML = xmlhttp.responseText;
								    }
								  }
			                    xmlhttp.open("GET",raven, true);
			                    xmlhttp.send();

							}
							});
							
							
							})
							
							
					});

			</script>
    
    </head>


    <body>

      
    	<button id="getval">Go</button>
      

    	<div id="display"></div>

		<form >

			<input id="i1" name="i1" value=""><br>
			<input id="i2" name="i2" value=""><br>
			<input id="i3" name="i3" value=""><br>
			<input id="i4" name="i4" value=""><br>
			<input id="i5" name="i5" value=""><br>
			<input id="i6" name="i6" value=""><br>
			<input id="i7" name="i7" value=""><br>
			<input id="i8" name="i8" value=""><br>
			<input id="i9" name="i9" value=""><br>
			<input id="i10" name="i10" value=""><br>
			<input id="i11" name="i11" value=""><br>
			<input id="i12" name="i12" value=""><br>
			<input id="i13" name="i13" value=""><br>
			<input id="i14" name="i14" value=""><br>
			<input id="i15" name="i15" value=""><br>
			<input id="i16" name="i16" value=""><br>

		</form>

    </body>

</html>

