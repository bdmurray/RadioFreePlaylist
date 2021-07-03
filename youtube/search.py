from youtubesearchpython import VideosSearch as yt_video_search

def search(artist, song):
    video_search = yt_video_search(artist + ' ' + song, limit = 1)
    return video_search.result()['result']