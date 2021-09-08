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
    response = service.files().list(q = " name contains 'tar.gz' and modifiedTime < '2020-11-20T12:00:00-08:00' " ,
                                          spaces='drive',
                                          fields='nextPageToken, files(id, name)',
                                          pageToken=page_token).execute()
    lista = []
    for file in response.get('files', []):
        lista.append(file.get('id'))
        print(file.get('name'), file.get('id'))
        
    for rec in lista:
        service.files().delete(fileId=rec).execute()
        print('Correctamente eliminado')

    page_token = response.get('nextPageToken', None)
    if page_token is None:
        break
    



 #service.trash() 
    #service.delete()
#    print(f'Fecha de eliminacion: {fecha}')

#"name contains 'zaphir_ee'
#name contains 'zaphir_' and name contains 'ee'
#and mimeType = 'application/x-tar'