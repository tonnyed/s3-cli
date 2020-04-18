from setuptools import setup, find_packages

setup(
    name="s3_cli",
    version="0.1.1",
    author="Tony Edogiawerie",
    description="s3 cli for uploading to aws s3",
    author_email ="tonnyed@hotmail.com",
    install_requires=['boto3'],
    entry_points={
        'console_scripts': [
            'teo=s3_cli.s3_main:main',
        ],
    },
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
