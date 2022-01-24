from bs4 import BeautifulSoup
import urllib.request
import stations.constants as const
import stations.helpers as helper
import json

#89.3 the current parsing
def parse():

    #read in and parse the contents of the KCMP playlist page
    html_page = urllib.request.urlopen(const.KCMP_URL)
    soup = BeautifulSoup(html_page, "html.parser")
    pl_json = soup.findAll('script', attrs={'id': '__NEXT_DATA__'})
    if (pl_json is not None):
        try:
            page_dict = json.loads(pl_json[0].string)
            pl_songs = page_dict['props']['pageProps']['data']['songs']
        except:
            pl_songs = []
    
    #setup a loop index and open a file to save first song id read 
    #song id will be used on subsequent runs to limit the loop to those already read/sent
    #file will be created if it doesn't exist
    idx = 0
    last_id = helper.get_kcmp_last_id()
    loop_id = None
    songs = []

    #KCMP uses the article tag for their playlist
    for pl_card in pl_songs:
        loop_time = loop_image = loop_title = loop_artist = ''

        #get ID of the song
        loop_id = str(pl_card['song_id'])

        #check to make sure we have an ID/valid tag.
        if (loop_id is not None):
            idx=idx+1
            #if this is the first article, grab the first article read last time and store our current id
            if (idx==1):         
                #store the first loop id to be used as the last id processed next run        
                helper.save_kcmp_last_id(loop_id)

            #check if the filesystem stored id is equal to this loop, if so, stop execution as we have already parsed/sent this
            if (last_id == loop_id): 
            #if (idx > 5):
                print('exiting loop, hit previous start.')
                break
            
            loop_title = str(pl_card['title']) #get the title of the song
            loop_artist = str(pl_card['artist']) #get the artist of the song
            loop_album = str(pl_card['album']) #get the album of the song
            loop_time = str(pl_card['played_at']) #get the time the song was played
            loop_image = str(pl_card['art_url']) #get the album art

            #print out the contents for testing, later to be replaced with api calls to create playlist
            songs.append(helper.song(loop_id, loop_time, loop_image, loop_artist, loop_title, loop_album))

    return songs
