import stations.kcmp as kcmp
import youtube.playlist as yt_playlist
import youtube.search as yt_search

def main():
    songs = kcmp.parse()

    #todo, store the playlist and check if 200 videos are found, rename based on date added / ended
    #maybe just KISS and do a playlist per day as actual limit is 5000, but shuffle stops working at 200
    playlist_id = yt_playlist.insert("KCMP Playlist", "Actual test, will replace", "public")
    print(playlist_id)

    #todo, figure out how to type/cast this so editor recognizes song class type, uhg, python....
    for songPlayed in songs:
        result = yt_search.search(songPlayed.artist, songPlayed.title)
        video_id = result[0]['id']
        print(songPlayed.artist + ' ' + songPlayed.title)
        print(video_id)
        yt_playlist.add_video_to_playlist(video_id, playlist_id)



if __name__ == "__main__":
    main()