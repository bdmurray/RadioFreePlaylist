import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import youtube.constants as const

def get_credentials():

    credentials = None

    # pickle file stores the user's credentials from previously successful logins
    if os.path.exists(const.YT_AUTH_FILE):
        #load credentials from file
        with open(const.YT_AUTH_FILE, 'rb') as token:
            credentials = pickle.load(token)

    # if there are no valid credentials available, then either refresh the token or log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            # refreshing access token...
            credentials.refresh(Request())
        else:
            # fetching new tokens
            flow = InstalledAppFlow.from_client_secrets_file(
                const.YT_CLIENT_SECRET, scopes=const.YT_MANAGE_SCOPE
            )

            flow.run_local_server(port=8080, prompt='consent', authorization_prompt_message='')
            credentials = flow.credentials

            # save the credentials for the next run
            with open(const.YT_AUTH_FILE, 'wb') as f:
                pickle.dump(credentials, f)

    return credentials