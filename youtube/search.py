import sys
from youtubesearchpython import VideosSearch as yt_video_search

def search(artist, song):
    try:
        video_search = yt_video_search(artist + ', ' + song, limit = 1)
        print("API:youtube search() " + artist + ', ' + song)
        return video_search.result()['result']
    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        print( "<p>Error: %s</p>" % e )
        return None