# sem1
import pytest
import requests

url_login = "https://test-stand.gb.ru/gateway/login"
url_posts = "https://test-stand.gb.ru/api/posts"
url_reg = "http://restapi.adequateshop.com/api/authaccount/registration"
url_login_api = "http://restapi.adequateshop.com/api/authaccount/login"

login = "Sixth Sense"
password = "81c597107f"

result = requests.post(url=url_login, data={
                       "username": login, "password": password})
token = result.json()["token"]

print(result)


res_get = requests.get(url="https://test-stand.gb.ru/api/posts", headers={
                       "X-Auth-Token": token}, params={"owner": "notMe"})
print(res_get)
print(res_get.json())
