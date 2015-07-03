$(document).ready(function() {
	//TODO: handle errors for words that don't have a hiden div.
	ORIGINAL_PARAGRAPH =  $("#original-paragraph p").html();

	if(typeof(Storage) !== "undefined") {
	    // Code for localStorage/sessionStorage.
	    localStorage.setItem("original_paragraph", ORIGINAL_PARAGRAPH);
	} else {
	    // Sorry! No Web Storage support..
	}

	
	$("#original-paragraph span").click(function() {
		word = $(this).text();
		$("ul[name=" + word+ "]").show();
	});
		
	$("#replacement-words span").click(function() {
		replacement_word = $(this).text();
		//console.log(replacement_word);
		// ew.
		parent_word = $(this).parent().parent().attr("name");


		orig_spans = $("#original-paragraph span");
		for (i=0; i < orig_spans.length; i++) {
			//TODO: replace the parent word with the replacement word
			if (orig_spans[i].innerHTML == parent_word) {
				$("#original-paragraph span").eq(i).html(replacement_word);
			}
		}		
	});
	
	function refreshParagraph() {
		$("#original-paragraph").html(localStorage.getItem("original_paragraph"));
	}

	$("button#refresh-paragraph").click(function() {
		refreshParagraph();
	})

});

/* grab the words and their positions from the original paragraph.
// log the positions for each word. 
