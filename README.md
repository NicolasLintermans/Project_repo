# first_python_projects

## Summary:
  - Project 0: getting started
  - Project 1: web scraping 
  - Project 2: scripting
  - Project 3: data science
  - Project 4: machine learning
    * Image analysis (flower iris) and prediction via scikit-learn
    * Image analysis (giraffe) and prediction via ImagePrediction library 
<br> 
<br>
## Project 0: Getting started
  - Syntax, functional programming (map, zip), OOP, decorators, classes and multiple inheritance. 

<br>

## Project 1: Web scraping
  - Since I'm sometimes tempted to read more articles on Hacker News than I perhaps should, I figured it would be a great exercise to scrape the website itself (via 
    BeautifulSoup). So, as of now, it only returns a limited amount of articles (those with a vote count of 500 and higher). 
<br>

## Project 2: Scripting
  - Note: I do NOT recommend passing your own password, as it is still stored 'somewhere'.
  - Scripting1: thumbnail images, convert them to PDFs, merge them into 1 PDF, watermark it and, finally, send a remote email as 'user notification'. Please also refer to
    user_notification.html.
  - Password checker via API: a requirement for the last part of previous project (sending remote emails) was to disable 'less secured apps' within Google user settings.
    Consequently, as it should, you receive a warning email from Google regarding the security of your account. As this is critical, a password checker via API may prove to be
    purposeful. 
<br>

## Project 3: Data science
  - Using pandas, seaborn and bokeh, I took a closer look at the FIFA_19 dataset (credits in the file). First, I displayed its #rows and #columns and the dataset's
    general statistics (#observations, mean, standard deviation etc.). As a way of exercising in getting more familiar in dealing with large datasets via Jupyter Notebook, 
    I filtered age > 40 and made a new column with the difference between player value and wage.
    
    To visualise the dataset, I opted for seaborn. First, I made a scatterplot of wage against value. Naturally, players with (relatively) high value but low wage are
    interesting to buy in the game. However, using this scatterplot would be time-consuming to draw conclusions, as it is not interactive (one would have to look it up in the
    dataset). So, to make this easier and more appealing, the visualisation could be made interactive using Bokeh. If you hover over the datapoints, the player's name, index,
    wage and value is displayed.
<br>

## Project 4: Machine learning
  - Flowers: using scikit-learn, a first glampse at machine learning was made possible. The available data was split into 20% test and 80% to train our model. The algorithm used 
    is kNN (k-nearest neighbors) for the classification with the amount of nearest datapoints (k) equal to 3 (since the dataset is very limited). Afterwards, the model is scored
    on its accuracy, which got between 96.67% and 100%. 
    The model was stored into joblib, so that the model could be called upon when needed (instead of needing it to run every
    time you run the file or (re)train the model). Finally, 2 examples were offered and the model was asked to predict what kind of iris it is.
    
  - Giraffe: using the ImagePrediction library and the Squeezenet model, the predictive results of a giraffe were ruffed grouse, prarie chicken, cheetah etc.
