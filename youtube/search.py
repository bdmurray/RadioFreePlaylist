from youtubesearchpython import VideosSearch

def search(artist, song):
    videosSearch = VideosSearch(artist + ' ' + song, limit = 2)

    print(videosSearch.result())