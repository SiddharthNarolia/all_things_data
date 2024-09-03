import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from creds.creds import storage_account_connection_string

# BlobServiceClient ----> Manipulate Azure Storage Blobs
# BlobClient ----> Manipulate Blobs
# ContainerClient ----> Manipulate Container


try:
    storage_client = BlobServiceClient.from_connection_string(storage_account_connection_string)

    #create demo container
    # container_name = 'testcontainer'
    # storage_client.create_container(container_name, public_access='BLOB')

    folder_path = 'C:/Users/siddg/Github/all_things_data/azure_demos/uploads'
    for file_name in os.listdir(folder_path):
        blob_obj = storage_client.get_blob_client(container='testcontainer',   blob=file_name)
        print('uploading files to container...')

        with open(os.path.join(folder_path, file_name), mode='rb') as file_data:
            blob_obj.upload_blob(file_data)



except Exception as e:
    print('Exception : \n')
    print(e)