import os
from datetime import datetime

DATABASE_NAME = 'US_VISA'

COLLECTION_NAME = 'visa_data'

MONGODB_URI_KEY = "MONGODB_URI"

PIPELINE_NAME = "usvisa"
ARTIFACT_DIR = "artifacts"

TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

FILE_NAME = "usvisa.csv"
MODEL_NAME = "model.pkl"

DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2