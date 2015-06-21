# MIDS-W205-A2

Mining Social Media Data Assignment
W205.3, Summer 2015

Deliverables:

1. A link to your S3 bucket documented in your README.md file. Make sure to make it publicly accessible.
The JSON files for the three use cases (#Warriors, #NBAFinals2015, and #Warriors AND #NBAFinals 2015) are found in the S3 bucket links below.

#Warriors  tweets (JSON files)
https://console.aws.amazon.com/s3/home?region=us-east-1#&bucket=june7_14_warriors_tweets&prefix=

#NBAFinals2015 tweets (JSON files)
https://console.aws.amazon.com/s3/home?region=us-east-1#&bucket=june7_14_nbafinals2015_tweets&prefix=

#Warriors and #NBAFinals2015 tweets (JSON files)
https://console.aws.amazon.com/s3/home?region=us-east-1#&bucket=june7_14_warriors_nbafinals2015_tweets&prefix=


2. Your twitter acquisition code.
The Twitter acquisition code is enclosed in the twitter_acq_forSubmission.py file.
This "for submission" version is a copy of the actual twitter_acq.py script that was used, but with the access keys/tokens removed.
To run this script, enter the following into your Command Prompt:
python twitter_acq.py "#Warriors"
python twitter_acq.py "#NBAFinals2015"
python twitter_acq.py "#Warriors #NBAFinals2015"

There is also a second Python script, historgram.py, was used to count the words from the tweets and create a histogram.

Some design decisions that were made:
- Acquire the tweets using the Twitter REST API
- Divide up acquired tweets into chunks of 100 tweets
- Parsed out the tweets into text files as the JSON files were created
    - This allowed for easier readability/faster analysis of tweets as they were coming in
- The Tweets were tokenized using NLTK and RegexpTokenizer
- The tokens were all changed to lower case and the stop words and emojis/none ASCII words were removed 
- A histogram of the top 30 words was created using matplotlib
- Pandas was also used to create a CSV files with a data frame of the tokens and counts


3. The histogram.

There are three files enclosed showing the histograms for each use case
- Histogram_Warriors.jpeg
- Histogram_NBAFinals2015.jpeg
- Histogram_Warriors_NBAFinals2015.jpeg

There are also three CSV files with the tokens and word counts for the top 30 words for each use case
- tweet_freq-Warriors.csv
- tweet_freq-NBAFinals2015.csv
- tweet_freq-Warriors_NBAFinals2015.csv
