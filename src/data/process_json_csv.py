import os
import json
import pandas as pd
import numpy as np
import time

from src.utils.execution_time import print_current_execution_time


def process_tracks_to_playlist_data(track, playlist_id):
    """
    With the track data process to generate the track/playlist relation.

    Args:
        track (dict): Song data of the Spotify Challenge Dataset
        playlist_id: # Playlist id to which the song belongs
    Returns:
        (array): [
            unique_playlist_trackorder_id: index per track_playlist relation,
            playlist_id: Playlist id to which the song belongs,
            track_id: Spotify unique track song id
        ]
    """
    unique_playlist_trackorder_id = f"{playlist_id}{track['pos']}"
    track_id = track['track_uri'][14:]

    return [unique_playlist_trackorder_id, playlist_id, track_id]


if __name__ == '__main__':
    # get the start time
    start_time = time.time()
    start_process_time = time.process_time()

    print('Started processing files')
    print('Finished processing files')
    print_current_execution_time(start_time, start_process_time)
