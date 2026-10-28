import requests

from .config import get_settings


IPINFO_URL = "https://ipinfo.io/json"


def get_ipinfo() -> dict:
    settings = get_settings()

    headers = {
        "Authorization": f"Bearer {settings.ipinfo_token}"
    }

    response = requests.get(
        IPINFO_URL,
        headers=headers,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()
