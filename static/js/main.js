$(document).ready(function() {
	//TODO: handle errors for words that don't have a hiden div.
	$("#original-paragraph span")
		.click(function() {
			word = $(this).text();
			$("ul[name=" + word+ "]").show();
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
			// ew.
			parent_word = $(this).parent().parent().attr("name");

			orig_spans = $("#original-paragraph span");
			for (i=0; i < orig_spans.length; i++) {
				//TODO: replace the parent word with the replacement word
				if (i.text() == parent_word) {
					$("#original-paragraph span").text(i).replace(word);
				}
			}

			
		});
});

