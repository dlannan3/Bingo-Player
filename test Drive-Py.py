from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaIoBaseDownload
import io

SCOPES = ['https://www.googleapis.com/auth/drive']

def download_file_from_drive(file_id, output_filename):
    # Set up credentials (assumes credentials.json is in your folder)
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    
    service = build('drive', 'v3', credentials=creds)
    
    # Request the file content
    request = service.files().get_media(fileId=file_id)
    
    # Open a local file to write the downloaded bytes into
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Download progress: {int(status.progress() * 100)}%")
        
    # Save the bytes to your local destination
    with open(output_filename, 'wb') as f:
        f.write(fh.getvalue())
        
    print(f"File downloaded successfully as '{output_filename}'!")

# Example: Download a specific file
# Replace 'YOUR_GOOGLE_DRIVE_FILE_ID' with the actual file ID from Google Drive
download_file_from_drive('1t20eof9j1-5N_Z6Cyz9et64kIg8MAFq_', 'Card1.jpg')