from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = Field(validation_alias="DATABASE_URL")
    app_title: str = "Kanban board"
    app_description: str = ("Kanban board - tablica kanban")
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


def get_settings() -> Settings:
    return Settings()