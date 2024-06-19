import requests
from requests.adapters import HTTPAdapter, Retry


def get_session():
    retry_strategy = Retry(
        total=5,
        backoff_factor=2,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "POST", "DELETE"],
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)

    session = requests.Session()
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    return session
