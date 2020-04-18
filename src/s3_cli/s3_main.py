





#invoking instance

def main():
    import os
    # from s3_upload import s3_upload
    # from s3_cli_upload import s3_cli_upload
    from s3_cli import s3_cli_upload
    from s3_cli import s3_upload
    from s3_cli import s3_set_aws_profile
    #s3 cli instance getters
    s3_cli_instance = s3_cli_upload.s3_cli_upload()
    file_name = s3_cli_instance['file_name']
    bucket_name = s3_cli_instance['bucket_name']
    object_name = s3_cli_instance['object_name']
    s3_arg = s3_cli_instance['s3_arg']
    aws_profile = s3_cli_instance['aws_profile']

# set aws env if --aws_profile is set
    if aws_profile != "none":
        s3_set_aws_profile.s3_set_aws_profile(aws_profile)
## logics #####
##checking there is a name error
    try:
        (file_name, bucket_name, object_name)
    except NameError:
        print("The required arguments is not defined")
    else:
        print("")

#using os walk to traverse and use control flow to check for file type

    if s3_arg == "s3":
        if os.path.isdir(file_name):

           for root, dirs, files in os.walk(file_name,topdown=False):
               for names in files:
                local_path = os.path.join(root, names)
                s3_upload.s3_upload(local_path ,bucket_name ,object_name, True)
        elif os.path.isfile(file_name):
            s3_upload.s3_upload(file_name,bucket_name,object_name)
        else:
           print("file is not a file or directory")

    else:
        print("s3 argument needs to be Specified")



