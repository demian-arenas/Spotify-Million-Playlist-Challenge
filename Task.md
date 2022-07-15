## 🎧 Task
The goal of the challenge is to develop a system for the task of automatic playlist continuation. Given a set of playlist features, participants' systems shall generate a list of recommended tracks that can be added to that playlist, thereby "continuing" the playlist. We define the task formally as follows:

### Input
* A user-created playlist, represented by:
    * Playlist metadata (see the dataset README)
    * K seed tracks: a list of K tracks in the playlist, where K can equal 0, 1, 5, 10, 25, or 100.

### Output
* A list of 500 recommended candidate tracks, ordered by relevance in decreasing order.

Note that the system should also be able to cope with playlists for which no initial seed tracks are given! To assess the performance of a submission, the output track predictions are compared to the ground truth tracks ("reference set") from the original playlist.