import pytest
import yaml
from task2 import get_token

@pytest.fixture(scope="session")
def auth_token():
    with open(r'E:\Учеба\Учусь\Automating Web Application Testing in Python\Sem1_Task2\config.yaml') as f:
        data = yaml.safe_load(f)
    token = get_token(data['url_login'], data['login'], data['password'])
    return token