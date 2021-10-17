""""connector and methods accessing s3"""
import os
import logging
import boto3
from boto3 import session


class S3BucketConnector():
    """
    class for interacting with s3 bucket
    """

    def __init__(self, accsess_key: str, secret_key: str, endpoint_url: str, bucket: str):
        """
        constructor for S3BucketConnector
        param accsess_key:accsess_key for s3 access
        param secret_key: secret_key for s3 access
        param endpoint_url:endpoint_url to s3
        param bucket :s3 bucket name
        """

        self._logger = logging.getLogger(__name__)
        self.endpoint_url = endpoint_url
        self.session = boto3.Session(aws_access_key_id=os.environ[accsess_key],
                                     aws_secret_access_key=os.environ[secret_key])

        # _s3 mean protected  variable.
        self._s3 = self.session.resource(
            service_name='s3', endpoint_url=endpoint_url)

        self._bucket = self._s3.Bucket(bucket)

    def list_files_in_prefix(self, prefix: str):
        """
        listing all files with a prefix on the s3 bucket
        :param prefix: prefix on s3 bucket that should be filtered with return:
        files: list of all the files names cintaining the prefix in the key
        """
        files = [obj.key for obj in self._bucket.objects.filter(Prefix=prefix)]
        return files

    def read_csv_to_df(self):
        pass

    def write_df_to_s3(self):
        pass
