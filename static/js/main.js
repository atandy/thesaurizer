$(document).ready(function() {
	
	ORIGINAL_PARAGRAPH =  $("#original-paragraph p").html();
	ORIGINAL_WORDS = $("#original-paragraph p span");

	// TODO: Handle what to do if no local storage for browser.
	if(typeof(Storage) !== "undefined") {
	    // Code for localStorage/sessionStorage.
	    localStorage.setItem("original_paragraph", ORIGINAL_PARAGRAPH);

	    for (i=0; i < ORIGINAL_WORDS.length; i++) {
	    	w = ORIGINAL_WORDS[i].innerHTML;
	    	w2 = w.replace(/[\.,-\/#!$%\^&\*;:{}=\-_`~()]/g,"");
			localStorage.setItem(w2, i.toString());
			try {
				if ($("ul[name=" + w2 + "]").length > 0) {
					$(ORIGINAL_WORDS[i]).addClass("linky");
				}
			}
			catch (e) {
			// silent exception caught here.
			}
		}	
	} else {
	    // Sorry! No Web Storage support..
	}
	
	// Handle clicks on words from original paragraph.
	$("#original-paragraph span").click(function() {
		// TODO: BUG, once a word has been replaced, you can't bring up the 
		// replacement UL, because it's trying to look up a UL that doesn't exist.
		word_to_replace = $(this).text();
		// remove any punctuation from word so it won't fail ul lookups.
		word_to_replace = word_to_replace.replace(/[\.,-\/#!$%\^&\*;:{}=\-_`~()]/g,"");
		
		if (word_to_replace.length <= 3) {
			return;
		}
		try {
			selected_ul = $("ul[name=" + word_to_replace + "]");
		} catch (e){
			console.log(e);
			return
		}
		// Hide all uls.. would be better to hide by kind, but this app is 
		// simple for now...
		$("ul").hide()
		$("#synonym-directions").hide()
		$(selected_ul).show();
		$("#synonym-directions").show()
		$(selected_ul).addClass('displayed');	
	});
		
	// Handle clicks on replacement words (synonyms)
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
	
	//TODO: Bug - refresh paragraph seems to lose all of the ul information.
	function refreshParagraph() {
		$("#original-paragraph p").html(localStorage.getItem("original_paragraph"));
		$("ul").hide()
		$("#synonym-directions").hide()
	}

	$("button#refresh-paragraph").click(function() {
		refreshParagraph();
	})

});