The aim of the project is
extract information from 
understand human mobility patterns
detect important events

Main assumptions we considered were:
1. We consider active users for mobility detection(at least threshold amount of tweets by the user)
2. We consider English tweets from 2016 for event detection since there are useful libraries for this task


### Mobility pattern

Main tools were geopandas and geojson files

Steps were following:
a)Data preprocessing
b)Data denoising( Here we remove the tweets if the location of user changed instantaneously from location a to b and back to a in a very 
short period by considering the ’speed of the tweets’ which means we remove the middle tweet if it does not make sense
fast location change)
c)Spatial indexing to find the states(we check if the location is inside particular region(canton) by checking if the point
is in polygon defined by that canton or region)
d) Find path and visualise it


### Event detection
Steps were following:
a)Read the tweets
b)Split data into half month portions(We need to find events in each time frame. Events dont last long)
c)Choose the portion corresponding to the desired time(The most common topic of tweets in a time frame can belong to the events for 
that time)
d)Find english tweets(there are 30 different languages used in tweets)
e)Normalize the texts(remove the stopwords,users,numbers,etc)
f)stem the texts
g)Find the clusters:
For clustering we use two algorithms:
  1) Cluster by kmeans
  2) Cluster by hierarchical clustering (see [1])
The best result found by second clustering model. This model is adaptive
and no hyper-parameter needs to be set initially.
The tweets contain weather prediction tweets, we remove them as they
are not an event.
Some of the events found by the algorithm using english tweets:
- We need help to save our show. Please help us sign and share thank
you.
- Hi friends please take few seconds to help us to save plz sign and
share thanks
- Yesterday One local outdoor pools transformed refugee camp people
Warning:
Clusters do not represent events necessarily, for example,
- Flirting messages!!!! my biggest dream is to wake up one day and see
your follow tysm for EVERYTHING, follow me pls, ilysm
- Weather predictions
