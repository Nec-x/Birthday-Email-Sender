from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
import own_variables as ov


def sheet_values():
    """
    Uses the Google Sheets API to call on a spreadsheet's ID to gather its information.
    """
    creds = None
    creds = service_account.Credentials.from_service_account_file(
        ov.specialkey_filename, scopes=['https://www.googleapis.com/auth/spreadsheets.readonly'])

    SAMPLE_SPREADSHEET_ID = ov.spread_id

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range = ov.spreadsheet_sheet_name).execute()
    values = result.get('values', [])

    return values
