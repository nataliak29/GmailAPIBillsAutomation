
from __future__ import print_function
import pickle
import os.path
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def connectToGmail():
    """Connect to Gmail API"""
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    
    if os.path.exists('credentials/token.pickle'):
        with open(os.path.join(sys.path[0],'credentials/token.pickle', 'rb')) as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.join(sys.path[0],'credentials/credentials.json'), SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(os.path.join(sys.path[0],'credentials/token.pickle', 'wb')) as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service


if __name__ == '__main__':
    connectToGmail()