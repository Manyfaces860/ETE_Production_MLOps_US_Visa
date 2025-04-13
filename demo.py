# import pymongo, os, pandas as pd
# import certifi
# from dotenv import load_dotenv
# from us_visa.constants import MONGODB_URI_KEY, DATABASE_NAME, COLLECTION_NAME
# load_dotenv()

# CONNECTION_URL = os.getenv(MONGODB_URI_KEY)
# print(CONNECTION_URL)
# client = pymongo.MongoClient(CONNECTION_URL, tlsCAFile=certifi.where())
# client = pymongo.MongoClient(CONNECTION_URL)
# data_base = client[DATABASE_NAME]
# collection = data_base[COLLECTION_NAME]

# print(collection)

# df = pd.read_csv("us_visa/notebooks/Visadataset.csv")
# print(df.head())

# data = df.to_dict(orient="records")
# data

# rec = collection.insert_many(data)

# df = pd.DataFrame(list(collection.find()))
# print(df.head())

from us_visa.pipeline.training_pipeline import TrainPipeline

pipe = TrainPipeline()
pipe.run_pipeline()

