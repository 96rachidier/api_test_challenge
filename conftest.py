# conftest.py

import pytest
from pages.import_api import ImportAPI
from dotenv import load_dotenv
import os
load_dotenv()

@pytest.fixture(scope="module")
def api():
    """
    Fixture global que devuelve una instancia de ImportAPI lista para usar en los tests.
    """
    print("API_BASE_URL:", os.getenv("BASE_URL"))
    base_url = os.getenv("BASE_URL")
    token = os.getenv("TOKEN")
    return ImportAPI(base_url, token)

