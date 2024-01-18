from google.oauth2 import service_account
from googleapiclient.discovery import build
from apiclient.http import MediaFileUpload,MediaIoBaseDownload

# Define the Google Drive API scopes and service account file path
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = "google_drive_key.json"

# Create credentials using the service account file
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the Google Drive service
drive_service = build('drive', 'v3', credentials=credentials)

def upload_File(filePath):
    media = MediaFileUpload(filePath, mimetype='*/*', resumable=True)
    file = drive_service.files().create(body={'name': filePath}, media_body=media).execute()

    drive_service.permissions().create(body={"role": "reader", "type": "anyone"}, fileId=file.get('id')).execute()
    file_metadata = drive_service.files().get(fileId=file.get('id'), fields="*").execute()

    return file_metadata['webContentLink']
