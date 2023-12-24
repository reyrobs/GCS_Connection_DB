# GCS_Connection_DB
Small program to connect to a database, and then upload the data to a bucket on GCS. The idea is to connect to a database named "test1.db", then extract, transform and load the data to a GCS bucket. In order to verify that the data was correctly added to GCS, we use a program to download the data and print the last row.
