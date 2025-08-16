from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):

    DATABASE_URL: str = "sqlite+aiosqlite:///./sql_app.db"
    SECRET_KEY: str
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    return Settings()
