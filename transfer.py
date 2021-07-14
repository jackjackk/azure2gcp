import googleapiclient.discovery
import json
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'google-credentials.json'

with open('google-credentials.json', 'r') as f:
    google_conf = json.load(f)

with open('azure-config.json', 'r') as f:
    azure_conf = json.load(f)

store_trans = googleapiclient.discovery.build('storagetransfer', 'v1')
trans_job = {
    'description': 'a desc',
    'status': 'ENABLED',
    'projectId': google_conf['project_id'],
    'transferSpec': {
    'azureBlobStorageDataSource': {
        'storageAccount': azure_conf['storage_account'],
        'azureCredentials': {
            'sasToken': azure_conf['sas_token']
            },
        'container': azure_conf['container'],
        }
    }
}

result = store_trans.transferJobs().create(body=trans_job).execute()
