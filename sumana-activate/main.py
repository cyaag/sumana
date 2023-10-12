import os, glob
from google.cloud import storage
# def getFromPI():

print("pi csv")

print("***3")
csv2_name = "/home/gautambh/var/tmp/sumana"
# csv2_name = "/var/tmp/sumana"
# for file in os.listdir(csv2_name):

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/gautambh/gcpkey.json"
# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = "sumana01"

destination_blob_name = "upload/"

bucket = storage_client.bucket(bucket_name)
print("instantiated the bucket")
# blob = bucket.blob(destination_blob_name)


for file in glob.glob(os.path.join(csv2_name, '*.txt')):
    print("file object = ", file.split("/")[6])
    file1 = file.split("/")[6]
    with open(os.path.join(os.getcwd(), file), 'r') as f:
        print("file name = ", file)
        print("End Reading one file")
        # blob = bucket.blob(destination_blob_name+"/"+file)
        # file = file.split(("/")[6])
        # print("file after  trim = ", file)
        # blob = bucket.blob(destination_blob_name+str(file1))
        blob = bucket.blob(str(file1))
        print("instantiated the destination folder")
        blob.upload_from_filename(file)
        print("finish uploading file")
print("Finished processing all files")