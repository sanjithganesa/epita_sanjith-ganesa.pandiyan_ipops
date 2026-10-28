import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    ipinfo_token: str


def get_settings() -> Settings:
    token = os.getenv("IPINFO_TOKEN")

    if not token:
        raise ValueError(
            "IPINFO_TOKEN environment variable is not set"
        )

    return Settings(ipinfo_token=token)
