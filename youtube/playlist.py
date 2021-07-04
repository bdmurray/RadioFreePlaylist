import os
import sys
from datetime import datetime
import pytz
import youtube.helpers as helper
import youtube.constants as const
from googleapiclient.discovery import build

def insert(title, description, privacy):

    credentials = helper.get_credentials()
    youtube = build(const.API_SERVICE_NAME, const.API_VERSION, credentials=credentials)

    body = dict(
        snippet=dict(
            title=title,
            description=description
        ),
        status=dict(
            privacyStatus=privacy
        ) 
    ) 

    try:
        playlists_insert_response = youtube.playlists().insert(
            part='snippet,status',
            body=body
        ).execute()

        #playlists_insert_response['id'] to get id
        return playlists_insert_response['id']
    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        print( "<p>Error: %s</p>" % e )
        return None

def delete(playlist_id):
    credentials = helper.get_credentials()
    youtube = build(const.API_SERVICE_NAME, const.API_VERSION, credentials=credentials)
    request = youtube.playlists().delete(id=playlist_id)
    try:
        request.execute()
    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        print( "<p>Error: %s</p>" % e )

def list(playlist_id):
    credentials = helper.get_credentials()
    youtube = build(const.API_SERVICE_NAME, const.API_VERSION, credentials=credentials)
    
    request = youtube.playlistItems().list(part=const.YT_LIST_RETURN, playlistId=playlist_id)

    try:
        response = request.execute()

        item_ids = []

        for item in response["items"]:
            vid_id = item['contentDetails']['videoId']
            item_ids.append(vid_id)
            #yt_link = f"https://youtu.be/{vid_id}"

        return item_ids

    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        print( "<p>Error: %s</p>" % e )
        return []

def add_video_to_playlist(video_id, playlist_id):
    credentials = helper.get_credentials()
    youtube = build(const.API_SERVICE_NAME, const.API_VERSION, credentials=credentials)
    request=youtube.playlistItems().insert(
        part="snippet",
        body={
            'snippet': 
                {
                    'playlistId': playlist_id, 
                    'resourceId': {
                        'kind': 'youtube#video',
                        'videoId': video_id
                    },
                    'position': 0
                }
        }
    )
    try:
        request.execute()
    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        print( "<p>Error: %s</p>" % e )

def get_playlist_id(station_name, station_description, station_timezone):
    #initialize the return
    playlist_id = None

    #get today's date (in the time zone of the station)
    current_date = datetime.now()
    timezone = pytz.timezone(station_timezone) 
    station_time = timezone.normalize(current_date.astimezone(timezone))

    #textual month, day and year	
    date_long = station_time.strftime("%B %d, %Y")

    #check if we already stored a playlist id for today in the file
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    #using w+ over r so it creates the file if it doesn't exist
    with open(os.path.join(file_dir, const.YT_DATAFOLDER + station_name + "-" + const.YT_DATAFILE), "w+") as data_file:
        data_file.seek(0)
        id_line = data_file.read()
        if (id_line != None and id_line != ''):
            #stored as date|id, so split and parse/compare to today's date
            date_id = id_line.split('|')
            if (len(date_id)==2):
                pl_date = date_id[0]
                pl_id = date_id[1]

                if (date_long == pl_date):
                    #use the same playlist id as the date hasn't changed
                    playlist_id = pl_id
                    print("using previous playlist " + playlist_id)
                else:
                    #create a new playlist for today's date
                    playlist_id = save_playlist_id(station_name, station_description, pl_date, data_file)
            else:
                #the playlist file was not empty and didn't have the appropriate contents, save a new playlist id
                playlist_id = save_playlist_id(station_name, station_description, date_long, data_file)
        else:
            #we either created the file or it was empty, save a new playlist id
            playlist_id = save_playlist_id(station_name, station_description, date_long, data_file)

    return playlist_id

def save_playlist_id(station_name, station_description, pl_date, data_file):
    #create the playlist
    playlist_id = insert(station_description + " " + pl_date, f"{station_name}: playlist for {pl_date}", "public")
    print("generated playlist for today: " + playlist_id)

    if (playlist_id != None):
        #store the playlist id over any previous ids
        pl_date_id = pl_date + "|" + playlist_id

        #save the playlist date/id based on station name
        #regardless of contents empty the file, we have stored or invalidated the id by this point
        data_file.seek(0)
        data_file.truncate() #had issues with truncate(0) appending characters to the start of the file so went with seek(0)/truncate
        
        #store the first id in the now empty file for next run
        data_file.write(pl_date_id)
    
    return playlist_id