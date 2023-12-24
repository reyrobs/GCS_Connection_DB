from google.cloud import storage
import os

# Instantiate a client to verify if the connection to the Bucket is successful
if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "GCS.json"
    storage_client = storage.Client()