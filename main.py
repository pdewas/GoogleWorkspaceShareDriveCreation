from __future__ import print_function
import httplib2
import os
import uuid

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from googleapiclient.discovery import build

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

def main():
	from oauth2client.service_account import ServiceAccountCredentials

	scopes = ['https://www.googleapis.com/auth/drive']

	credentials = ServiceAccountCredentials.from_json_keyfile_name('sakey.json', scopes)
	http = credentials.authorize(httplib2.Http())

	delegated_credentials = credentials.create_delegated('email@domain.com')
	http_auth = delegated_credentials.authorize(httplib2.Http())

	drive_service = build('drive', 'v3', http=http_auth)
	
	drive_metadata = {'name': 'Hello mon petit'}
	request_id = str(uuid.uuid4())
	drive = drive_service.drives().create(body=drive_metadata,requestId=request_id,fields='id').execute()
	print('Drive ID: %s' % drive.get('id'))
	

if __name__ == '__main__':
    main()