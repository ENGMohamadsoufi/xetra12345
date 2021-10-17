"""
file to store constants
"""
from enum import Enum


class S3FilesTypes(Enum):

    CSV = 'csv'
    PARQUET = 'parquet'


class MetaProcessFormat(Enum):
    """
    information metaprocess class
    """
    META_DATE_FORMAT = '%Y-%m-$d'
    META_PROCESS_DATE_FORMAT = '%Y-%m-$d %H:M:S'
    META_SOURCE_DATE_COL = 'source_date'
    META_PROCESS_COL = 'datetime_of_processing'
    META_FILE_FORMAT = 'csv'
