from bs4 import BeautifulSoup
import urllib.request

html_page = urllib.request.urlopen("https://www.thecurrent.org/playlist")
soup = BeautifulSoup(html_page, "html.parser")

idx = 0


for article in soup.findAll('article'):
    idx=idx+1
    loopId = article.get('id')
    loopTime = ''
    loopImage = ''
    loopTitle = ''
    loopArtist = ''

    if (loopId is not None):
        for time in article.findAll('time'):
            if (len(time) > 0): loopTime = time.string.strip()
        for img in article.findAll('img',  {"class":"album-art"}):
            if (img['src']):
                loopImage = 'https://www.thecurrent.org/' + img['src']
            elif (img['data-src']):
                loopImage = img['data-src']
            else:
                loopImage = ''
        for title in article.findAll("h5",  {"class":"title"}):
            if (len(title) > 0): loopTitle = title.string.strip()
        for artist in article.findAll("h5",  {"class":"artist"}):
            if (len(artist) > 0): loopArtist = artist.string.strip()
        print (loopId + ',' + loopTime + ',' + loopImage + ' ,' + loopArtist + ',' + loopTitle)
