from __future__ import print_function

import os
import os.path
import pickle
import warnings

from google.auth.transport.requests import Request

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1HidYOx3PacMlm3rLyaFOKO5uldM7Lo4NGLS9SLkXY9Q'
SAMPLE_RANGE_NAME = 'Dictionnaire!A2:B'


# if __name__ == '__main__':
#     path = sys.argv[1]
#     target_lang = sys.argv[2]
#     api_result = detect(path)
#
#     write_on_image(path, api_result, target_lang, 'out.png')
#
#
#     sys.exit(0)


def get_credentials():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds


def get_spreadsheet_content():
    """
    Shows basic usage of the Sheets API.
    """
    creds = get_credentials()

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        warnings.warn('No data found in spreadsheet!')
        return {}

    word_dict = dict([{row[0], row[1]} for row in values])
    print("Got word dictionnary.")
    return word_dict


if __name__ == '__main__':
    get_spreadsheet_content()
