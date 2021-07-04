import stations.kcmp as kcmp
import youtube.playlist as yt_playlist
import youtube.search as yt_search

def main():
    #parse the current song list, this function will store the first id read to avoid double saving songs
    songs = kcmp.parse()

    #check for a stored playlist for today's date for this station, if one doesn't exist, create it.
    playlist_id = yt_playlist.get_playlist_id("KCMP", "The Current 89.3")
    print(playlist_id)

    #todo, figure out how to type/cast this so editor recognizes song class type, uhg, python....
    for songPlayed in songs:
        #search for the song, take the top result for now
        #todo: features like live performances, seeing if there is a way to find major labels, etc
        result = yt_search.search(songPlayed.artist, songPlayed.title)
        if (result != None):
            video_id = result[0]['id']
            print(songPlayed.artist + ' ' + songPlayed.title)
            print(video_id)

            #add the video to the playlist for station/today
            yt_playlist.add_video_to_playlist(video_id, playlist_id)
        else:
            print("error adding: " + songPlayed.artist + ' ' + songPlayed.title)

if __name__ == "__main__":
    main()