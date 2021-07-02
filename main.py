import stations.kcmp as kcmp

def main():
    songs = kcmp.parse()

    #todo, figure out how to type/cast this so editor recognizes song class type, uhg, python....
    for songPlayed in songs:
        print(songPlayed.artist)

if __name__ == "__main__":
    main()