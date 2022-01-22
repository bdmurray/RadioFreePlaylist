import os
import stations.constants as const

class song: 
    def __init__(self, id, time, image, artist, title, album): 
        self.id = id 
        self.time = time
        self.image = image
        self.artist = artist
        self.title = title
        self.album = album

def get_kcmp_last_id():
    #get the id for KCMP stored in the data file
    last_id = 0
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    with open(os.path.join(file_dir, const.KCMP_DATAFILE), "r") as data_file:
        data_file.seek(0)
        id_line = data_file.read()
        if (id_line is not None):
            if (id_line.isnumeric()):
                last_id = id_line
    return last_id

def save_kcmp_last_id(last_id):
    #save the id for KCMP in the data file
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    with open(os.path.join(file_dir, const.KCMP_DATAFILE), "w") as data_file:
        #regardless of contents empty the file, we have stored or invalidated the id by this point
        data_file.seek(0)
        data_file.truncate() #had issues with truncate(0) appending characters to the start of the file so went with seek(0)/truncate
        
        #store the first id in the now empty file for next run
        data_file.write(last_id)