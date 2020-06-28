



# Methods



## Data extraction

For the consecution of this project we extracted 
* 120K tweets from the 40 main business association accounts in Spain
* 269K tweets from the 35 main companies in spain (ibex 35) in Spain
* 17K tweets from the 30 main business association accounts in Perú
* 72K tweets from the 20 main companies in spain (ibex 35) in Spain

These tweets cover the period dated from january 2017 to march 2020.

In order to train a spanish sentiment analysis neural network we also extracted 100K rated user reviews. This reviews covered very variated items such as films, products and places and were extracted using *web crawling* software in public websites.

## Spanish sentiment analysis neural networks training using reviews data
Using the 100K rated reviews in spanish we separated them in two groups: *positive reviews* and *negative reviews*. Since there were more positive than negative reviews, we balanced the two classes removing enough positive ones to have the same size in both groups.

For the neural network architecture  we used an embedding layer, four convolutional (1 dimensional) layers, two poolings and a one dimensional output dense layer. Other architectures were tried, but we obtained poorer results in terms of validation accuracy.

|data |accuracy | precission  | recall  |
|-|-|-|-|-|
|training data| 0.9988  | 0.9991  |  0.9992 |  
|test data (validation) | 0.9869  |  0.9840 |  0.9870 


## Tweets processing using sentiment analysis

Using the neural network sentiment model described in the previous section, we proceed with the analysis and of the tweets from the business associations and companies using the following steps:

1. We run the sentiment analysis on each tweet. This gives us a number between 0 and 1 expressing the positivity or negativity of the tweet.
2. We calculate the average of all the tweets published in the same day in each group.
3. We calculate the difference between the average sentiment in each given day and the day before to remove the trend component and make the data more comparable.

This transforms the data into a time series that we can study and compare to macro economic data. In particular we obtain four time series: daily sentiment of main comanies and business associations both in Spain and Peru.

The four time series are the starting point in our analysis and modeling process. See figure 1

![](plots_sentiment.png) 
**figure 1**


# Results

## Prediction of Madrid and Lima stocks change using traditional models

We use the daily average sentiment data described in the previous section to predict the fluctuations of stock values.

First, we see that the daily average sentiment is a stationary time series ()


## Prediction of Madrid and Lima stocks change using neural networks models



