# SMoji
A Twitter bot that shows the weather in Sweden as a map of emojis. Inspired by @TweeteoFrance

—————————————————————————————————————————————————————————————————————————————————————————————


The smoji.py script uses the functions in SMoji_functions.py to
  * fetch the weather symbols for 77 places in Sweden from the SMHI API
  * convert these symbols into emojis
  * place them in a matrix so the shape looks like a map of Sweden
  * send it on Twitter
  
grid.csv contains the latitude and longitude of 77 points positioned on a grid covering the map of Sweden. A few points have been corrected by hand (Gotland, Riksgränsen)

weatheremoji.xlsx contains two sheets
  * emojis that maps the SMHI weather symbols to corresponding emojis
  * mappix a matrix of 0s and 1s where a 0 codes for a white space and 1 for a point in Sweden
  
