from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):

    JWT_SECRET: str = os.environ.get("JWT_SECRET","default_pass")
    JWT_ALGORITHM: str = os.environ.get("JWT_ALGORITHM", "HS256")
    JWT_TOKEN_EXPIRE_MIN: int = int(os.environ.get("JWT_TOKEN_EXPIRE_MIN", 10))