import argparse

def s3_cli_upload():
    s3_local = argparse.ArgumentParser()
    s3_local.add_argument("s3", help="used to s3 upload")
    s3_local.add_argument("--file-name", help="used to set file name")
    s3_local.add_argument("--bucket-name", help="used to set s3 bucket name")# parser = argparse.ArgumentParser()
    s3_local.add_argument("--object-name", help="used to set s3 object, if not set, file name will be used", default="none")
    s3_local.add_argument("--aws-profile", help="use the flag to set aws profile env, for example prod", default="none")


    args= s3_local.parse_args()
    aws_profile = args.aws_profile
    file_name = args.file_name
    bucket_name = args.bucket_name
    object_name = args.object_name
    return {'file_name': file_name, 'bucket_name': bucket_name, 'object_name': object_name, 's3_arg': args.s3, 'aws_profile': aws_profile}