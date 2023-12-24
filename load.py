import pandas as pd
import os
from google.oauth2 import service_account

'File to load the csv file to GCP bucket'

def load_to_GCP(data):
    gcs_bucket = 'e_commerce_de'
    gcs_file_path = 'E_Commerce/e_commerce_data.csv'
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/GCS.json"
    credentials = service_account.Credentials.from_service_account_file("GCS.json",
                                                                        scopes=["https://www.googleapis.com/auth/cloud-platform"])
    data.to_csv(f'gcs://{gcs_bucket}/{gcs_file_path}', index=False, storage_options={'token': credentials})

if __name__ == '__main__':
    df = pd.read_csv('clean_dataframe.csv')
    load_to_GCP(df)