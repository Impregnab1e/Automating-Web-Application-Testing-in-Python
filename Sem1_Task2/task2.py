import requests
import yaml


def get_data():
    with open(r'E:\Учеба\Учусь\Automating Web Application Testing in Python\Sem1_Task2\config.yaml') as f:
        data = yaml.safe_load(f)
    return data


def get_token(url_login, login, password):
    result = requests.post(url=url_login, data={"username": login, "password": password})
    return result.json()["token"]

def get_posts(token, url_posts):
    res_get = requests.get(url=url_posts, headers={"X-Auth-Token": token}, params={"owner": "notMe"})
    return res_get.json().get('data', [])