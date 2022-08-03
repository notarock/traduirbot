#!/usr/bin/env python3
from __future__ import print_function

import os
import os.path
import pickle
import warnings
import json

from google.auth.transport.requests import Request

from config import Config
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.

words_file = "resources/words.json"

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
                'credentials.json', Config.get_instance().get_config('SCOPES'))
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
    result = sheet.values().get(spreadsheetId=
                                Config.get_instance()
                                .get_config('SPREADSHEET_ID'),
                                range=
                                Config.get_instance()
                                .get_config('RANGE_NAME')).execute()

    values = result.get('values', [])

    if not values:
        warnings.warn('No data found in spreadsheet!')
        return {}

    print("rows")
    if values[0][0] == 'en':
        word_dict = dict([{row[0], row[1]} for row in values])
    else:
        word_dict = dict([{row[1], row[0]} for row in values])

    print(word_dict)
    return word_dict

def get_dict():
    try:
        content = open(words_file, 'r').read()
        return json.loads(content)
    except IOError:
        dump_to_file()
        content = open(words_file, 'r').read()
        return json.loads(content)

def dump_to_file():
    results = get_spreadsheet_content()
    with open(words_file, 'w') as outfile:
        json.dump(results, outfile)

if __name__ == '__main__':
    dump_to_file()
