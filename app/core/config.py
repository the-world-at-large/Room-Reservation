from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Название проекта по умолчанию'
    app_description: str = 'Описание проекта по умолчанию'
    database_url: str

    class Config:
        env_file = '.env'


settings = Settings()
