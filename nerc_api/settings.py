from pydantic_settings import BaseSettings, SettingsConfigDict


class NERCSettings(BaseSettings):

    MODEL_NAME: str = None
    STRIDE: int = 100
    AGGREGATION_STRATEGY: str = "simple"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = NERCSettings()
