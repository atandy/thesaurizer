$(document).ready(function() {
	//TODO: handle errors for words that don't have a hiden div.
	$("#original-paragraph span")
		.click(function() {
			word = $(this).text();
			$("ul." + word).show();
		});
		/*
		.mouseout(function(){
			$("ul." + word).hide();
		});
		*/
	$("#replacement-words span")
		.click(function() {
			word = $(this).text();
			console.log(word);

			
		});
});

