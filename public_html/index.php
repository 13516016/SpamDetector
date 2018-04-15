<!DOCTYPE html>
<html>
<head>
	<title><?php print("Twitter Spam Detector")?></title>
	<link rel="stylesheet" type="text/css" href="css/style.css">
	<link href="https://fonts.googleapis.com/css?family=Do+Hyeon|Roboto" rel="stylesheet">
	<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">

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
					<input type="text" name="" placeholder="Search">
				</div>

				<div class="navbar-search-spam">
					<p>Enter the spam keyword</p>
					<input type="text" name="" placeholder="Spam Keyword">
				</div>

				<div class="navbar-search-algorithm">
					<p>Choose a method</p>
					<select>
						<?php  
							function generate_option($value)
							{
								return "<option value=\"$value\">$value</option>";
							}

							$algorithms = array("Knuth-Morris-Pratt", "Boyer Moore", "Regular Expression");

							foreach ($algorithms as $algorithm) {
								$option = generate_option($algorithm);
								print($option);
							}

					 	?>
					</select>
				</div>

				<div class="navbar-search-submit">
					<button>
						Search
					</button>
				</div>
			</div>

			</div>

		<div class="content"></div>
	</div>
<!-- 	

		<?php 
			$algorithms = array("Knuth-Morris-Pratt", "Boyer Moore", "Regular Expression");
			foreach ($algorithms as $algorithm) {
				print("<h1>"); print("$algorithm"); print("</h1>");
			}
		?> -->

	</div>
	 <script type="text/javascript" src="js/api.js"></script>
</body>
</html>