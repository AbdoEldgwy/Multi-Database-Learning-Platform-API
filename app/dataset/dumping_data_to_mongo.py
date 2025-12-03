import pandas as pd
from app.models.mongo_models import MongoProduct
from app.db.mongo import db
import asyncio

def load_from_csv_without_id(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, encoding='latin-1')
    df.drop(columns=['id'], inplace=True)
    return df

async def dump_data_to_mongo(df: pd.DataFrame, mongo_collection: str) -> None:
    records = df.to_dict(orient='records')
    await db[mongo_collection].insert_many(records)

    # print(f"Dumping {len(records)} records to MongoDB...,\n sample record: {records[0:2]}")


asyncio.run(dump_data_to_mongo(load_from_csv_without_id(r'app\dataset\ProductDataset.csv'), 'products'))