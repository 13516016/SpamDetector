// Class definition
class Tweet {
	constructor(text, handle, name, isSpam) {
		this.text = text;
		this.handle = handle;
		this.name = name;
		this.isSpam = isSpam;
	}

	generateView(){

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
	json_data = {
	    "algorithm" : selectedAlgorithm,
	    "searchkey" : search_keyword,
	    "spamkey" : spam_keyword
  	}

  	contentLoader.show();
	$.ajax({
		url: 'http://127.0.0.1:5000/kmp',
		type: 'POST',
		data: JSON.stringify(json_data),
		contentType: 'application/json',
		success: function(result){
			response = JSON.parse(result);
			tweets = parseTweets(response);
			for (var i = 0; i < tweets.length; i++) {
				tweets[i].print();	  
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