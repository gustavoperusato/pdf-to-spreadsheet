from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from pprint import pprint
from googleapiclient import discovery

SCOPES = [
     'https://www.googleapis.com/auth/drive',
     'https://www.googleapis.com/auth/drive.file',
     'https://www.googleapis.com/auth/spreadsheets'
]
creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

def sendData (data,sheetId,range,insert_data_option):

    service = discovery.build('sheets', 'v4', credentials=creds)

    # How the input data should be interpreted.
    value_input_option = 'RAW'  # TODO: Update placeholder value.

    value_range_body = {
        
            'values': data 
    }

    request = service.spreadsheets().values().append(spreadsheetId=sheetId, range=range, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
    response = request.execute()

    # TODO: Change code below to process the `response` dict:
    pprint(response)
    
def getData (sheetId,range):
    
    service = discovery.build('sheets', 'v4', credentials=creds)
    
    # How values should be represented in the output.
    # The default render option is ValueRenderOption.FORMATTED_VALUE.
    value_render_option = 'UNFORMATTED_VALUE'  # TODO: Update placeholder value.

    # How dates, times, and durations should be represented in the output.
    # This is ignored if value_render_option is
    # FORMATTED_VALUE.
    # The default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER].
    date_time_render_option = 'FORMATTED_STRING'  # TODO: Update placeholder value.

    request = service.spreadsheets().values().get(spreadsheetId=sheetId, range=range, valueRenderOption=value_render_option, dateTimeRenderOption=date_time_render_option)
    response = request.execute()

    # TODO: Change code below to process the `response` dict:
    return response

def getSheetInfo (sheetId,range):

    service = discovery.build('sheets', 'v4', credentials=creds)

    # True if grid data should be returned.
    # This parameter is ignored if a field mask was set in the request.
    include_grid_data = False  # TODO: Update placeholder value.

    request = service.spreadsheets().get(spreadsheetId=sheetId, ranges=range, includeGridData=include_grid_data)
    response = request.execute()

    # TODO: Change code below to process the `response` dict:
    return response

def updateData (data,sheetId,range):
    from pprint import pprint

    from googleapiclient import discovery

    # TODO: Change placeholder below to generate authentication credentials. See
    # https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
    #
    # Authorize using one of the following scopes:
    #     'https://www.googleapis.com/auth/drive'
    #     'https://www.googleapis.com/auth/drive.file'
    #     'https://www.googleapis.com/auth/spreadsheets'

    service = discovery.build('sheets', 'v4', credentials=creds)

    # How the input data should be interpreted.
    value_input_option = 'RAW'  # TODO: Update placeholder value.

    value_range_body = {
        # TODO: Add desired entries to the request body. All existing entries
        'values': data
    }

    request = service.spreadsheets().values().update(spreadsheetId=sheetId, range=range, valueInputOption=value_input_option, body=value_range_body)
    response = request.execute()

    # TODO: Change code below to process the `response` dict:
    pprint(response)