from google.cloud import storage
import os

def get_last_modified_object(bucket_name):
    # Create a client to interact with Google Cloud Storage
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "GCS.json"
    client = storage.Client()

    # Get the specified bucket
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob('E_Commerce/e_commerce_data.csv')
    # Download the contents of the CSV file to the specified local destination path
    blob.download_to_filename('e_commerce_data.csv')

    with open('e_commerce_data.csv', 'r') as file:
        data = file.readlines()
    lastRow = data[-1]
    print(lastRow)

    os.remove('e_commerce_data.csv')

if __name__ == '__main__':
    get_last_modified_object('e_commerce_de')