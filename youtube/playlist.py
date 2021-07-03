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
    
    playlists_insert_response = youtube.playlists().insert(
        part='snippet,status',
        body=body
    ).execute()

    #playlists_insert_response['id'] to get id
    return playlists_insert_response['id']

def delete(playlist_id):
    credentials = helper.get_credentials()
    youtube = build(const.API_SERVICE_NAME, const.API_VERSION, credentials=credentials)
    request = youtube.playlists().delete(id=playlist_id)
    request.execute()

def list(playlist_id):
    credentials = helper.get_credentials()
    youtube = build(const.API_SERVICE_NAME, const.API_VERSION, credentials=credentials)
    
    request = youtube.playlistItems().list(part=const.YT_LIST_RETURN, playlistId=playlist_id)

    response = request.execute()

    item_ids = []

    for item in response["items"]:
        vid_id = item['contentDetails']['videoId']
        item_ids.append(vid_id)
        #yt_link = f"https://youtu.be/{vid_id}"

    return item_ids

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
    request.execute()