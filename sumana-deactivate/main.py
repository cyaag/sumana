import os, glob
from google.cloud import storage
# def getFromPI():

print("pi csv")

print("***3")
csv2_name = "/home/gautambh/var/tmp/sumana/deactivate"
# csv2_name = "/var/tmp/sumana/deactivate"
# for file in os.listdir(csv2_name):

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/gautambh/gcpkey.json"
# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name2 = "sumana02"

destination_blob_name = "upload/"

bucket = storage_client.bucket(bucket_name2)
print("instantiated the bucket")
bucket2 = storage_client.bucket(bucket_name2)
blob = list(bucket2.list_blobs())

for file in blob:
    print("file = ", str(file).split(",")[1])
    # file.download_to_filename('/var/tmp/sumana-web')
    # file.download_to_filename('/home/gautambh/var/tmp/sumana-web'+"/"+str(file).split(",")[1])
    print("End Reading one file from GCP")
    print("file name from GCP = ", str(file).split(",")[1])
    file.download_to_filename('/home/gautambh/var/tmp/sumana/deactivate' + "/" + str(file).split(",")[1])
    print("finish downloading files from GCP")
print("Finished processing all files")