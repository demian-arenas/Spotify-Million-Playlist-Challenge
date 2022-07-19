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


def process_tracks_to_set_tracks(track):
    """
    Process the track song data to add the Spotify Song id and delete playlist order position.

    Args:
        track (dict): Song data of the Spotify Challenge Dataset
    Returns:
        Track (dict): Track song dict with the Spotify unique track song id
    """
    track_id = track['track_uri'][14:]
    del track['pos']
    track['track_id'] = track_id

    return track


def process_playlist(playlist):
    """
    Clean each playlist dict extracting the tracks key. 
    Then process tracks to generate the unique_tracks and track_playlist relation datasets.

    Args:
        playlist (dict): Playlist dict of the Spotify Challenge Dataset
    Returns:
        (dict): {
            playlist_tracks (pd.DataFrame): DataFrame with the track/playlist relation,
            unique_tracks (pd.DataFrame): DataFrame with the uniques tracks,
            playlist (dict): Playlist dict without the tracks section.
        }
    """
    unique_tracks_columns = ["artist_name", "track_uri", "artist_uri",
                             "track_name", "album_uri", "duration_ms", "album_name", 'track_id']
    track_to_playlist_columns = [
        'unique_playlist_trackorder_id', 'playlist_id', 'track_id']

    playlist_id = playlist['pid']
    tracks_in_playlist = playlist['tracks']
    del playlist['tracks']

    tracks_to_playlist_data = [process_tracks_to_playlist_data(
        track=track, playlist_id=playlist_id) for track in tracks_in_playlist]
    playlist_tracks = pd.DataFrame(
        data=tracks_to_playlist_data, columns=track_to_playlist_columns)

    processed_unique_tracks = [process_tracks_to_set_tracks(
        track=track) for track in tracks_in_playlist]
    unique_tracks = pd.DataFrame(
        data=processed_unique_tracks, columns=unique_tracks_columns)
    return {
        'playlist_tracks': playlist_tracks,
        'unique_tracks': unique_tracks,
        'playlist': playlist
    }


if __name__ == '__main__':
    # get the start time
    start_time = time.time()
    start_process_time = time.process_time()

    print('Started processing files')
    print('Finished processing files')
    print_current_execution_time(start_time, start_process_time)
