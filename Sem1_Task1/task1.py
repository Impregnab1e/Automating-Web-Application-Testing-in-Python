from zeep import Client, Settings
import yaml


# url = "https://speller.yandex.net/services/spellservice?WSDL"
# settings = Settings(strict=False)
# client = Client(wsdl=url, settings=settings)
# print(client.service.checkText("tabll"))


with open(r'E:\Учеба\Учусь\Automating Web Application Testing in Python\Sem1_Task1\config.yaml') as f:
    data = yaml.safe_load(f)


def check_word(word):
    url = data["url"]
    settings = Settings(strict=False)
    client = Client(wsdl=url, settings=settings)
    return client.service.checkText(word)[0]['s']
