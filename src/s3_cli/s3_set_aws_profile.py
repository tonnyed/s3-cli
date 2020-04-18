import os

#set aws profile environment

def s3_set_aws_profile(s3_env):
    os.environ["AWS_PROFILE"] = s3_env
    print("AWS_PROFILE SET TO"+" "+os.environ["AWS_PROFILE"])
    return True

