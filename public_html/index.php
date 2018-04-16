<!-- <?php header('Access-Control-Allow-Origin: *'); ?> -->

<!DOCTYPE html>
<html>
<head>
	<title><?php print("Twitter Spam Detector")?></title>
	<link rel="stylesheet" type="text/css" href="css/style.css">
	<link href="https://fonts.googleapis.com/css?family=Do+Hyeon|Roboto" rel="stylesheet">
	<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>


</head>
<body>
	<div class="header">
		<div class="header-about">
			 <span>About</span>
		</div>

	</div>
	<div class="container">
		<div class="navbar">

			<div class="navbar-search">
				<div class="navbar-search-tweet">
					<p>Search tweets</p>
					<input type="text" name="tweetInput" placeholder="Search Twitter" id="input_tweet">
				</div>

				<div class="navbar-search-spam">
					<p>Enter the spam keyword</p>
					<input type="text" name="spamInput" placeholder="Spam Keyword" id="input_spam">
				</div>

				<div class="navbar-search-algorithm">
					<p>Choose a method</p>
					<select name="algorithm_selector" id="select_algorithm">
						<?php  
							function generate_option($value, $text)
							{
								return "<option value=\"$value\">$text</option>";
							}

							$algorithms_text = array("Knuth-Morris-Pratt", "Boyer Moore", "Regular Expression");
							$algorithms_val = array("kmp", "bm", "regex");

							for ($i = 0; $i < sizeof($algorithms_val); $i++) {
								$option = generate_option($algorithms_val[$i],$algorithms_text[$i]);
								print($option);
							}

					 	?>
					</select>
				</div>

				<div class="navbar-search-submit">
					<button id="button_search">
						Search
					</button>
				</div>
			</div>

			</div>

		<div class="content">
			
			
			<div class="content-header"> <span>Result</span>  </div>
			<div class="content-loader" id="content_loader"></div>
			

		</div>

	</div>
	 <script type="text/javascript" src="js/api.js"></script>
</body>
</html>