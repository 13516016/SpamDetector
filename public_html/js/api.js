// Class definition
class Tweet {
	constructor(text, handle, name, isSpam) {
		this.text = text;
		this.handle = handle;
		this.name = name;
		this.isSpam = isSpam;
	}

	generateView(){
		/*construct tweet outer div*/
		var tweetDiv = $("<div></div>");
		tweetDiv.addClass('tweet');
		
		/*construct tweet status div*/
		var tweetStatusDiv = $("<div></div>");
		tweetStatusDiv.addClass('tweet-status')

		// tweet status content
		var icon = $("<i></i>");
		icon.addClass('fa fa-2x');
		var status = $("<span></span>");
		var newline = $("<br>");
		if (this.isSpam){
			tweetStatusDiv.addClass('spam');
			icon.addClass('fa-warning');
			status.text('Spam');
		} else {
			tweetStatusDiv.addClass('notspam');
			icon.addClass('fa-check');
			status.text('Not Spam');
		}

		  
		/*Tweet Content*/
		var tweetContentDiv = $("<div></div>");
		tweetContentDiv.addClass('tweet-content');
		// tweet full name
		var fullname = $("<span></span>");
		fullname.addClass('tweet-content-name');
		fullname.text(this.name);
		// tweet handle
		var handle = $("<span></span>");
		handle.addClass('tweet-content-handle');
		handle.text(this.handle);
		// tweet content text
		var contentText = $("<p></p>");
		contentText.text(this.text);

		tweetContentDiv.append(fullname,' - ', handle, contentText);
		tweetStatusDiv.append(icon,newline,status)
		tweetDiv.append(tweetStatusDiv, tweetContentDiv);
		return (tweetDiv);
	}

	print(){
		console.log("Username : " + this.handle);
		console.log("Display name : " + this.name);
		console.log("Content : " + this.text);
		console.log("Spam : " + this.isSpam);
	}
}

// Elements
var inputTweet = $("#input_tweet");
var inputSpam = $("#input_spam");
var selectAlgorithm = $("#select_algorithm");
var buttonSearch = $("#button_search");
var contentLoader = $("#content_loader");
var contentPlaceholder = $("#content_placeholder");
var content = $("#content_tweet");
var tweets = [];


// hide loader
contentLoader.hide();

// Functions
function parseTweets(tweetObjects){
	var tweets = [];
	for (var i = 0; i < tweetObjects.length; i++) {
		tweetObject = tweetObjects[i];
		text = tweetObject['text'];
		handle = tweetObject['screen_name'];
		nama = tweetObject['full_name'];
		isSpam = tweetObject['is_spam'];
		tweet = new Tweet(text,handle,nama,isSpam);
		tweets.push(tweet);
	}
	return tweets;
}

function getTweets(search_keyword,spam_keyword,algorithm){
  	var targetUrl = 'http://127.0.0.1:5000/';

	json_data = {
	    "algorithm" : selectedAlgorithm,
	    "searchkey" : search_keyword,
	    "spamkey" : spam_keyword
  	}
  	contentLoader.show();
  	contentPlaceholder.hide();
  	
  	if (algorithm == "kmp"){
  		targetUrl += "kmp";
  	} else if (algorithm == "bm"){
  		targetUrl+= "bm";
  	} else if (algorithm == "regex"){
  		targetUrl += "regex";
  	}

	$.ajax({
		url: targetUrl,
		type: 'POST',
		data: JSON.stringify(json_data),
		contentType: 'application/json',
		success: function(result){
			var response = JSON.parse(result);
			
			tweets = parseTweets(response);
			
			if (tweets.length==0){
				contentPlaceholder.show();
			}

			for (var i = 0; i < tweets.length; i++) {
				var tweetObject = tweets[i].generateView();	  
				content.prepend(tweetObject);
			}
		},
		error: function(result){
			alert("Something is wrong");
		},
		complete: function(){
			contentLoader.hide();
			
		}

	});	
}

buttonSearch.click(function() {
	selectedAlgorithm = selectAlgorithm.find(":selected").val();
	searchInput = inputTweet.val();
	spamInput = inputSpam.val();

	getTweets(searchInput, spamInput, selectedAlgorithm);
});

// NOT SPAM
// 	<div class="tweet">
// 		<div class="tweet-status notspam">
// 			<i class="fa fa-check fa-2x "></i>
// 			<br>
// 			<span>Not Spam</span>
// 		</div>
// 		<div class="tweet-content">
// 			<span class="tweet-content-name">
// 				Adylan Roaffa Ilmy
// 			</span>
// 			- 
// 			<span class="tweet-content-handle">
// 				@odidang
// 			</span>

// 			<p>
// 			</p>
// 		</div>
// 	</div>
// </div>

// SPAM
// <div class="tweet-status spam">
// 		<i class="fa fa-warning fa-2x"></i>
// 		<br>
// 		<span>Spam</span>
// 	</div>
// 	<div class="tweet-content">
// 		<span class="tweet-content-name">
// 			Adylan Roaffa Ilmy
// 		</span>

// 		- 

// 		<span class="tweet-content-handle">
// 			@odidang
// 		</span>

// 		<p>
// 		Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
// 		tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
// 		quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
// 		consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
// 		cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
// 		proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
// 		</p>
// 	</div>