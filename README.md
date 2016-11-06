This is the repository for the final project of ADA course.

# Project proposal(initial draft version):
## Mobility patterns/events in Switzerland with Twitter

### Abstract
Understanding human mobility patterns is crucial for traffic management and urban planning. In this project, we aim to extract useful information from a collection of geo-located Twitter messages. A significant advantage of utilizing the geo-located Twitter messages as a platform for studying human mobility patterns is the large spatial coverage. Many recent studies have taken advantage of these kinds of data streams to study human mobility patterns. For example, they modeled and extracted trajectories of individuals to reveal different travel modes [1], travel demands [2], and the impact of social connections [3].

### Data Description
The possible initial goal of this project is to extract tweets from twitter. We are not sure whether for this project the data are provided by you or we ourselves should do that. But in general, it would be fun to do data extraction phase.

### Goals and Deliverables
1. The first goal of this project is to show that geo-located tweets can capture rich features of human mobility, such as the diversity of movement orbits among individuals and of movements between cities. More specifically, we plan to extract high-frequency migration patterns in Switzerland. An example of these high-frequency migration patterns may be observed from the frontiers who commute from France to Geneva or from Germany to Zurich every day.

2. The second goal of this project is to detect the possible change in the mobility patterns after constructing a new highway or tunnel. One example which is worthwhile to consider is the change in mobility patterns after the construction of the new Alpine tunnel in Switzerland. To do so, we need a metric to measure the distance between probability distribution functions; i.e., the probability distribution function before and after the construction. We plan to consider Kolmogorov-Smirnov test to measure this distance. Moreover, in this context, the Earth Mover distance or Wasserstein distance can be very informative as it takes into account the whole shape of probability distribution functions. It is straightforward to show that computing earth mover distance can be done using linear programming solvers. 

3. The third goal of this project is to extract good and bad things in each city in Switzerland in order to provide some useful information for a newcomer tourist. This information can be interpreted as some kind of online review of each city. Moreover, based on the total tweets about a city, we can set a rating to the city. Hence, it is much easier for a tourist to determine his priorities for different places in Switzerland.

4. The fourth goal of this project is to show the difference between mobility patterns in different seasons in Switzerland. Namely, we would like to observe which areas are more popular in Summer and which ones are more attractive during Winter. One can also extend this goal to study the mobility pattern on weekends and weekdays or to study the mobility patterns in specific days such as Christmas or Easter holidays.This data also can be used for telecommunication providers to manage their resources more efficiently or to manage the traffic in a more efficient way.

5. The final goal of the project is to develop a model which can predict the heaviness of a traffic. We believe the problem can be formulated as a Markov chain [4], then the classical result of the Markov chain can be applied to the setting. More precise, we can model the cities as the states of the Markov chain and the transition probability between these states can be considered as the traffic heaviness.

### Timeplan
 Our goal in this project is to finish as many points described above as possible in the two months period specified, however, based on the difficulty of the problem some of the points might not be finished in the limited time we have. 
 Here is our time plan and risk measure for the project:
* **Data cleaning:** A good portion of the project might be the time spend for cleaning and preparing the data. We plan to finish this part of the project in 2-3 weeks.

* **Pattern extraction**: This part of the project corresponds to the points 1-4 described above. We plan to extract the mobility patterns from the data in 1 week, build a suitable distance measure for two different mobility patterns and different pattern detector in 1 week, detect the time based temporal and permanent patterns of the mobility 1 week.

* **Theoretical studies:** This part of the project corresponding to the point 5 is the most challenging  and risky part and depends on the time we have left. We plan to take the  initial steps in this direction and continue our studies based on the plausibility of the results.

[1] Jurdak, Raja, et al. "Understanding human mobility from Twitter." PloS one 10.7 (2015): e0131469.

[2] Wu, Lun, et al. "Intra-urban human mobility and activity transition: Evidence from social media check-in data." PloS one 9.5 (2014): e97010.

[3] Cho, Eunjoon, et al. "Friendship and mobility: user movement in location-based social networks." Proceedings of the 17th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, 2011.

[4] Akinori, Asahara, et al. “Pedestrian-movement Prediction based on Mixed Markov-chain Model.” GIS '11 Proceedings of the 19th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems



