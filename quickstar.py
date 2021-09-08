from os import remove
from Google import Create_Service
from datetime import date
from datetime import datetime
from datetime import timedelta
import fnmatch

CLIENT_SECRET_FILE = "Client_secret.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

fecha = datetime.now().strftime('%y-%m-%d_%H:%M:%S')
page_token = None


while True:
    response = service.files().list(q = " name contains 'tar.gz' and modifiedTime < '2021-08-06T12:00:00-08:00' and modifiedTime > '2021-07-10T12:00:00-08:00'" ,
                                          spaces='drive',
                                          fields='nextPageToken, files(id, name)',
                                          pageToken=page_token).execute()
    lista = []
    for file in response.get('files', []):
        lista.append(file.get('id'))
        print(file.get('name'), file.get('id'))
        service.files().delete(fileId=file.get('id')).execute()
        print('Correctamente eliminado')
        

    page_token = response.get('nextPageToken', None)
    if page_token is None:
        break
    


