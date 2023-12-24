from extract import *
import numpy as np
import pandas as pd

'File to clean and transform the Data before Loading'

countries = [
 'Australia',
 'Austria',
 'Bahrain',
 'Belgium',
 'Brazil',
 'Canada',
 'Channel Islands',
 'Cyprus',
 'Czech Republic',
 'Denmark',
 'EIRE',
 'European Community',
 'Finland',
 'France',
 'Germany',
 'Greece',
 'Hong Kong',
 'Iceland',
 'Israel',
 'Italy',
 'Japan',
 'Lebanon',
 'Lithuania',
 'Malta',
 'Netherlands',
 'Norway',
 'Poland',
 'Portugal',
 'RSA',
 'Saudi Arabia',
 'Singapore',
 'Spain',
 'Sweden',
 'Switzerland',
 'USA',
 'United Arab Emirates',
 'United Kingdom',
 'Unspecified']

def clean(df):
    df1_temp = df.copy()
    df1_temp = df1_temp.dropna()
    df_clean = df1_temp[df1_temp['CustomerID'] != '']
    df_clean = df_clean[df_clean.Country.isin(countries)]
    df_clean = df_clean.astype({"InvoiceNo": str, "StockCode": str, "Description": str,
                                "Quantity": int, "InvoiceDate": str, "UnitPrice": float, "CustomerID": int,
                                "Country": str
                                })
    return df_clean


if __name__ == '__main__':
    data = extract_from_sqlite('test1.db', 'e_commerce')
    column_names = get_col_names('test1.db', 'e_commerce')
    df1 = pd.DataFrame(np.array(data), columns=column_names)
    df_clean = clean(df1)
    df_clean.to_csv('clean_dataframe.csv', encoding='utf-8', index=False)