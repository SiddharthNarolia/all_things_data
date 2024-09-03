from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient, generate_blob_sas, BlobSasPermissions
from azure.identity import DefaultAzureCredential
import pandas as pd
from creds.creds import storage_account_connection_string, storage_account_key
from datetime import datetime, timedelta

account_name = 'snaroliastorage'
container_name = 'snaroliacontainer'

storage_client = BlobServiceClient.from_connection_string(storage_account_connection_string)
container_client = storage_client.get_container_client(container_name)

blob_list = []
for blob_i in container_client.list_blobs():
    blob_list.append(blob_i.name)

for blob_i in blob_list:
    sas_i = generate_blob_sas(account_name=account_name, 
                              container_name=container_name,
                              blob_name=blob_i,
                              account_key=storage_account_key,
                              permission=BlobSasPermissions(read=True),
                              expiry=datetime.now() + timedelta(hours=1))
    print(sas_i)
    sas_url = f'https://{account_name}.blob.core.windows.net/{container_name}/{blob_i}?{sas_i}'
    print(sas_url)
    
    df = pd.read_csv(sas_url)