import stations.kcmp as kcmp
import youtube.playlist as yt_playlist
import youtube.search as yt_search

def main():
    songs = kcmp.parse()

    #todo, figure out how to type/cast this so editor recognizes song class type, uhg, python....
    for songPlayed in songs:
        yt_search.search(songPlayed.artist, songPlayed.title)
        print(songPlayed.artist + ' ' + songPlayed.title)

    # yt_playlist.insert("Another Test", "Just a test from the function", "public")


if __name__ == "__main__":
    main()