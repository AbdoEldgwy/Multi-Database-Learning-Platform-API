from dotenv import load_dotenv
import os

load_dotenv()
# print(os.environ)  

class Settings:
    POSTGRES_HOST  = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")

    MONGO_URI = os.getenv("MONGO_URI")

    REIST_HOST = os.getenv("REIST_HOST")
    REIST_PORT = os.getenv("REIST_PORT")

settings = Settings()
