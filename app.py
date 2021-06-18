from bs4 import BeautifulSoup
import urllib.request

#read in and parse the contents of the KCMP playlist page
html_page = urllib.request.urlopen("https://www.thecurrent.org/playlist")
soup = BeautifulSoup(html_page, "html.parser")

#setup a loop index and open a file to save first song id read 
#song id will be used on subsequent runs to limit the loop to those already read/sent
#file will be created if it doesn't exist
idx = 0
fileId = open("last-id.txt", "r+")
lastId = None
loopId = None

#KCMP uses the article tag for their playlist
for article in soup.findAll('article'):
    loopId = article.get('id')
    loopTime = ''
    loopImage = ''
    loopTitle = ''
    loopArtist = ''

    #check to make sure we have an ID/valid tag.
    if (loopId is not None):
        idx=idx+1
        #if this is the first article, grab the first article read last time and store our current id
        if (idx==1): 
            fileId.seek(0)
            idLine = fileId.read()
            if (idLine is not None):
                if (idLine.isnumeric()):
                    lastId = idLine
            
            #regardless of contents empty the file, we have stored or invalidated the id by this point
            fileId.seek(0)
            fileId.truncate() #had issues with truncate(0) appending characters to the start of the file so went with seek(0)/truncate
            
            #store the first id in the now empty file for next run
            fileId.write(loopId)

        #check if the filesystem stored id is equal to this loop, if so, stop execution as we have already parsed/sent this
        if (lastId == loopId): 
            print('exiting loop, hit previous end. lastId:' + lastId + ' loopId:' + loopId)
            break
        
        #get the time the song was played
        for time in article.findAll('time'):
            if (len(time) > 0): loopTime = time.string.strip()
        
        #get the album art, handle different image tag issues we found parsing the content.
        for img in article.findAll('img', {"class":"album-art"}):
            if (img['src']):
                loopImage = 'https://www.thecurrent.org' + img['src']
            elif (img['data-src']):
                loopImage = img['data-src']
            else:
                loopImage = ''
        
        #get the title of the song
        for title in article.findAll("h5", {"class":"title"}):
            if (len(title) > 0): loopTitle = title.string.strip()

        #get the artist of the song
        for artist in article.findAll("h5", {"class":"artist"}):
            if (len(artist) > 0): loopArtist = artist.string.strip()

        #print out the contents for testing, later to be replaced with api calls to create playlist
        print (loopId + ',' + loopTime + ',' + loopImage + ' ,' + loopArtist + ',' + loopTitle)

#close the file that stores our id
fileId.close()
