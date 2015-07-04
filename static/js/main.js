$(document).ready(function() {
	//TODO: handle errors for words that don't have a hiden div.
	ORIGINAL_PARAGRAPH =  $("#original-paragraph p").html();
	ORIGINAL_WORDS = $("#original-paragraph p span");

	if(typeof(Storage) !== "undefined") {
	    // Code for localStorage/sessionStorage.
	    localStorage.setItem("original_paragraph", ORIGINAL_PARAGRAPH);

	    for (i=0; i < ORIGINAL_WORDS.length; i++) {
			localStorage.setItem(ORIGINAL_WORDS[i].innerHTML, i.toString());
		}	
	} else {
	    // Sorry! No Web Storage support..
	}
	/*
	for (i=0; i<ORIGINAL_WORDS.length; i++) {
		if ($("ul[name=" + ORIGINAL_WORDS[i].innerHTML + "").length > 0 {
			$("#original-paragraph span");
		}
	}
	*/

	$("#original-paragraph span").click(function() {
		
		word_to_replace = $(this).text();
		selected_ul = $("ul[name=" + word_to_replace + "");
		// Hide all uls.. would be better to hide by kind, but this app is 
		// simple for now...
		$("ul").hide()
		$("#synonym-directions").hide()
		$(selected_ul).show();
		$("#synonym-directions").show()
		$(selected_ul).addClass('displayed');	

		
	});
		
	$("#replacement-words span").click(function() {
		replacement_word = $(this).text();
		//console.log(replacement_word);
		// ew.
		parent_word = $(this).parent().parent().attr("name");

		// for the parent word, get the position from local storage.
		parent_word_position = localStorage.getItem(parent_word);
		
		// replace the word based on its position.
		$("#original-paragraph span").eq(parent_word_position).html(replacement_word);
		
	});
	
	function refreshParagraph() {
		$("#original-paragraph p").html(localStorage.getItem("original_paragraph"));
		$("ul").hide()
		$("#synonym-directions").hide()
	}

	$("button#refresh-paragraph").click(function() {
		refreshParagraph();
	})

});

/* grab the words and their positions from the original paragraph.
log the positions for each word. */
