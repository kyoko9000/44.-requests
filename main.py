from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = "Credentials.json"
API_SERVICE_NAME = "drive"
API_VERSION = "v3"
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

folder_id = "1eZ_CGHhv7Jow8FBP4u1ViEmyIXLW1DXK"
file_names = ["1.jpeg", "2.jpeg"]
file_tyles = ["image/jpeg", "image/jpeg"]

# for file_name, file_tyle in zip(file_names, file_tyles):
for file_name in file_names:
    file_metadata = {
        "name": file_name,
        "parents": [folder_id]
    }
    media = MediaFileUpload("pics/icons/{0}".format(file_name), resumable=True)  # , mimetype=file_tyle
    send = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()
    print('File ID: %s' % send.get('id'))
