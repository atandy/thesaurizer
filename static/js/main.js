$(document).ready(function() {
	//TODO: handle errors for words that don't have a hiden div.
	$("span")
		.mouseover(function() {
			word = $(this).text();
			$("ul." + word).show();
		})
		.mouseout(function(){
			$("ul." + word).hide();
		});
});

