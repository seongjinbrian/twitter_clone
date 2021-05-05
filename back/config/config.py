import os
from pathlib import Path
from pydantic import BaseSettings


class Settings(BaseSettings):
    # db info
    db_host: str
    db_port: int
    db_database: str
    db_user: str
    db_password: str

    # server
    port: str

    class Config:
        env_file = f'{Path(os.path.dirname(__file__))}/dev.env'
        env_file_encoding = 'utf-8'
        case_sensitive = False


config = Settings()