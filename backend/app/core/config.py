from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from functools import lru_cache
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(CURRENT_DIR, ".env")


class Settings(BaseSettings):

    DEBUG: bool = True

    DATABASE_URL: str

    AI_MODE: str = "mock"  # mock | letta
    # Letta settings
    LETTA_API_KEY: SecretStr
    LETTA_ENVIRONMENT: str = "cloud"  # cloud | local
    LETTA_AGENT_NAME: str = "sitesage-seo-agent"
    LETTA_MODEL_CLOUD: str = "openai/gpt-4o-mini"
    LETTA_MODEL_LOCAL: str = "ollama"

    model_config = SettingsConfigDict(env_file=ENV_PATH, extra="ignore")


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
