from pydantic import BaseSettings, Field


class ServiceDatabaseSettings(BaseSettings):
    host: str = "localhost"
    username: str = "admin"
    password: str = "admin"
    db_name: str = Field(default="begemotic", env="service_db_name")
    port: int = Field(default="5432")

    class Config:
        allow_mutation = False
        env_prefix = "service_db_"
        # env_file = '.env'
        # env_file_encoding = 'utf-8'

    @property
    def postgresql_url(self) -> str:
        print(f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}")
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}"


service_database_settings = ServiceDatabaseSettings()
