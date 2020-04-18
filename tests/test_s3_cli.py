# RED > GREEN > REFACTOR
import pytest
from s3_cli import s3_cli_upload
from s3_cli import s3_upload

@pytest.fixture
def s3_cli_instance():
    return s3_cli_upload.s3_cli_upload()

file_name = "file"
bucket = "edogiawere"
@pytest.fixture
def s3_upload_instance(file_name, bucket):
    # file_name = "file"
    # bucket = "edogiawere"
    return s3_upload.s3_upload(file_name, bucket)


s3 = "s3"
def test_s3_cli_parser_s3(s3_cli_instance):

    with pytest.raises(SystemExit):
        cli = s3_cli_instance
        s3_cli = cli.parse_args(s3)
        arg_s3 = cli['s3_arg']
        arg_s3 == "s3"




def test_s3_upload(s3_upload_instance):
    get = s3_upload_instance
    assert get == True

# def test_s3_cli_parameter():
#     cli = s3_cli_upload.s3_cli_upload()
#     s3_cli = cli.parse_args(s3)
#     assert s3_cli == "s3"