# DataMiningOnlineShoppingReviews
#######################################################################################
# Measurement of Customer Satisfaction Using User Comments of Products on Online Shopping Sites
### Kagan Yavuz
#

***	A simple interface has been designed for the project in C#.

You can run the program by opening the "DataMiningOnlineShoppingReviews.exe" application from the "DataMiningOnlineShoppingReviews" folder and clicking on the "Get Dataset" - "Sentiment Analysis" and "Keyword Analysis" buttons sequentially, and view the results on the screen.
#
***	To run the project without the interface:

The project consists of three stages:

1- Using Python Selenium to fetch user reviews from Amazon.com and save them into a .txt file.

2- Performing sentiment analysis on the created .txt file using the Python TextBlob library.

3- Performing keyword analysis on the created .txt file using the Python NLTK library after removing
unnecessary words and conjunctions from the dataset, and then using the Python TextBlob library.

1) Using Python Selenium to fetch user reviews from Amazon.com and save them into a .txt file:

In the first stage, after installing python, selenium, and chromedriver on the computer where the code will be run, the "SeleniumProjectToGetData" project should be opened. The executable path of the chromedriver previously installed on the computer should be provided on line 10 of the main.py code of the relevant project.

Then, when the main.py code of the relevant project is run, it will be seen that a file named "user_reviews.txt" is created in the main directory of the project. This file contains user reviews of the product from the Amazon.com link provided on line 17 of the main.py code. 

After creating the "user_reviews.txt" file by following these steps, you can proceed to the second stage.

2) Performing sentiment analysis on the created .txt file using the Python TextBlob library:

In the second stage of the project, sentiment analysis is performed. The "user_reviews.txt" file created in the first stage should be copied to the main directory of the "TextBlobProjectToSentimentAnalysis" project and the main.py code of the "TextBlobProjectToSentimentAnalysis" project can be directly run. 

As an output of this project, the following values will be found:
- Sentiment Score (polarity)
- Sentiment Label
- Subjectivity

3) Performing keyword analysis on the created .txt file using the Python NLTK library after removing unnecessary words and conjunctions from the dataset, and then using the Python TextBlob library:

In the third stage of the project, keyword analysis is performed. The "user_reviews.txt" file created in the first stage should be copied to the main directory of the "TextBlobProjectToKeywordAnalysis" project and the main.py code of the "TextBlobProjectToKeywordAnalysis" project can be directly run.
	
As an output of this project, the following values will be found:
- The most used words in the dataset
- The most used 2-word phrases in the dataset
- The most used 3-word phrases in the dataset
#
Thank you,

Kagan Yavuz
