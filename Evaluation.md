## 🖊 Evaluation
Submissions will be evaluated using the following metrics. All metrics will be evaluated at both the track level (exact track match) and the artist level (any track by the same artist is a match).

In the following, we denote the ground truth set of tracks by  and the ordered list of recommended tracks by . The size of a set or list is denoted by , and we use from:to-subscripts to index a list. In the case of ties on individual metrics, earlier submissions are ranked higher.

### R-PRECISION
R-precision is the number of retrieved relevant tracks divided by the number of known relevant tracks (i.e., the number of withheld tracks):


The metric is averaged across all playlists in the challenge set. This metric rewards total number of retrieved relevant tracks (regardless of order).

### NORMALIZED DISCOUNTED CUMULATIVE GAIN (NDCG)
Discounted Cumulative Gain (DCG) measures the ranking quality of the recommended tracks, increasing when relevant tracks are placed higher in the list. Normalized DCG (NDCG) is determined by calculating the DCG and dividing it by the ideal DCG in which the recommended tracks are perfectly ranked:


The ideal DCG or IDCG is, in our case, equal to:


If the size of the set intersection of  and  is empty, then the IDCG is equal to 0. The NDCG metric is now calculated as:


### RECOMMENDED SONGS CLICKS
Recommended Songs is a Spotify feature that, given a set of tracks in a playlist, recommends 10 tracks to add to the playlist. The list can be refreshed to produce 10 more tracks. Recommended Songs clicks is the number of refreshes needed before a relevant track is encountered. It is calculated as follows:


If the metric does not exist (i.e. if there are no relevant tracks in , a value of 51 is picked (which is 1 greater than the maximum number of clicks possible).

### RANK AGGREGATION
Final rankings will be computed by using the Borda Count election strategy. For each of the rankings of p participants according to R-precision, NDCG, and Recommended Songs Clicks, the top ranked system receives p points, the second system received p-1 points, and so on. The participant with the most total points wins. In the case of ties, we use top-down comparison: compare the number of 1st place positions between the systems, then 2nd place positions, and so on.