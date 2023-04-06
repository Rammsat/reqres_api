import pytest
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def set_up_env():
    load_dotenv()
