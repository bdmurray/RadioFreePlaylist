from bs4 import BeautifulSoup
import urllib.request
import stations.constants as const
import stations.helpers as helper

#89.3 the current parsing
def parse():

    #read in and parse the contents of the KCMP playlist page
    html_page = urllib.request.urlopen(const.KCMP_URL)
    soup = BeautifulSoup(html_page, "html.parser")

    #setup a loop index and open a file to save first song id read 
    #song id will be used on subsequent runs to limit the loop to those already read/sent
    #file will be created if it doesn't exist
    idx = 0
    last_id = helper.get_kcmp_last_id()
    loop_id = None
    songs = []

    #KCMP uses the article tag for their playlist
    for article in soup.findAll('article'):
        loop_id = article.get('id')
        loop_time = loop_image = loop_title = loop_artist = ''

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
            
            #get the time the song was played
            for time in article.findAll('time'):
                if (len(time) > 0): loop_time = time.string.strip()
            
            #get the album art, handle different image tag issues we found parsing the content.
            for img in article.findAll('img', {"class":"album-art"}):
                if (img['src']):
                    loop_image = const.KCMP_ROOT + img['src']
                elif (img['data-src']):
                    loop_image = img['data-src']
                else:
                    loop_image = ''
            
            #get the title of the song
            for title in article.findAll("h5", {"class":"title"}):
                if (len(title) > 0): loop_title = title.string.strip()

            #get the artist of the song
            for artist in article.findAll("h5", {"class":"artist"}):
                if (len(artist) > 0): loop_artist = artist.string.strip()

            #print out the contents for testing, later to be replaced with api calls to create playlist
            songs.append(helper.song(loop_id, loop_time, loop_image, loop_artist, loop_title))

    return songs
