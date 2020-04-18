import boto3
from pathlib import Path
from botocore.exceptions import ClientError
import os
import sys
import threading
import datetime


# this class is used to read the progress
class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()




#This function uses boto3 s3 resource with upload methods
def s3_upload(file_name, bucket_name, object_name="none", dir=True):
    s3 = boto3.client('s3')
    object_name = object_name
    object_date = datetime.datetime.now()
    object_date =object_date.strftime("%d-%m-%Y-%H-%M-%S")


    if object_name == "none" and dir == False:
        object_name = file_name+"-"+object_date

    elif object_name == "none" and dir == True:
        object_name = file_name
        object_name = str(Path(object_name+"-"+object_date))

    elif dir == True and object_name != "none":
        object_name = file_name
        object_name = str(Path(object_name+"-"+object_date))
        print("using directory name as object name!")

    else:
        object_name = Path(object_name)
        object_name = str(object_name)


    try:
        response = s3.upload_file( file_name, bucket_name, object_name, Callback=ProgressPercentage(file_name))
    except ClientError as e:
        logging.error(e)
        return False

    print("complete!")
    return True

