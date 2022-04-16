from __future__ import print_function

import io
import json
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive']


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
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

    try:
        service = build('drive', 'v3', credentials=creds)

        # ............upload file.....................
        folder_id = "1eZ_CGHhv7Jow8FBP4u1ViEmyIXLW1DXK"
        file_names = ["1.jpeg", "h hh.mp4"]
        for file_name in file_names:
            file_metadata = {
                "name": file_name,
                "parents": [folder_id]
            }
            media = MediaFileUpload("pics/icons/{0}".format(file_name), resumable=True)
            send = service.files().create(
                body=file_metadata,
                media_body=media,
                fields="id"
            ).execute()
            print('File ID: %s' % send.get('id'))

        # ..........download file...............
        # file_id = '1vDlTDB9-csR_MThBwdA23vOUmL2DTIzp'
        # request = service.files().get_media(fileId=file_id)
        # fh = io.BytesIO()
        # downloader = MediaIoBaseDownload(fh, request)
        # done = False
        # while done is False:
        #     status, done = downloader.next_chunk()
        #     print("Download %d%%." % int(status.progress() * 100))
        #     with open("C:/Users/DELL/Desktop/New folder/test.mp4", "wb") as f:
        #         f.write(fh.getvalue())

        #  .............get link google............
        # Update Sharing Setting
        # file_id = '1vDlTDB9-csR_MThBwdA23vOUmL2DTIzp'
        #
        # request_body = {
        #     'role': 'reader',
        #     'type': 'anyone'
        # }
        #
        # response_permission = service.permissions().create(
        #     fileId=file_id,
        #     body=request_body
        # ).execute()
        #
        # print(response_permission)
        #
        # # Print Sharing URL
        # response_share_link = service.files().get(
        #     fileId=file_id,
        #     fields='webViewLink'
        # ).execute()
        #
        # print(response_share_link)
        print("complete")
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()
