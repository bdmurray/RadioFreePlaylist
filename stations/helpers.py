import stations.constants as const
import os

class song: 
    def __init__(self, id, time, image, artist, title): 
        self.id = id 
        self.time = time
        self.image = image
        self.artist = artist
        self.title = title

fileDir = os.path.dirname(os.path.realpath('__file__'))

def get_kcmp_last_id():
    lastId = 0
    with open(os.path.join(fileDir, const.KCMP_DATAFILE), "r") as data_file:
        data_file.seek(0)
        idLine = data_file.read()
        if (idLine is not None):
            if (idLine.isnumeric()):
                lastId = idLine
    return lastId

def save_kcmp_last_id(lastId):
    with open(os.path.join(fileDir, const.KCMP_DATAFILE), "w") as data_file:
        #regardless of contents empty the file, we have stored or invalidated the id by this point
        data_file.seek(0)
        data_file.truncate() #had issues with truncate(0) appending characters to the start of the file so went with seek(0)/truncate
        
        #store the first id in the now empty file for next run
        data_file.write(lastId)