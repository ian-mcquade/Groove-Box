
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    sound_cloud_client_id: str
    sound_cloud_client_secret: str
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()
