import yaml
import time
from module import Site

with open(r"E:\Учеба\Учусь\Automating Web Application Testing in Python\Sem2_Selenium\testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


def test_step1(log_xpath, pass_xpath, btn_xpath, result_xpath):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys("test")
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys("test")
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    err_lable = site.find_element("xpath", result_xpath)
    assert err_lable.text == "401"


def test_step2(site, log_xpath, pass_xpath, btn_xpath, result_login):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    login = site.find_element("xpath", result_login)
    assert login.text == "Blog"


def test_step3(site, log_xpath, pass_xpath, btn_xpath):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()

    create_button = site.find_element("xpath", '//*[@id="create-btn"]')
    create_button.click()
    input_field = site.find_element(
        "xpath", '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    input_field.send_keys("Здесь могла бы быть ваша реклама")
    save_button = site.find_element(
        "xpath", '//*[@id="create-item"]/div/div/div[7]/div/button/span')
    save_button.click()

    time.sleep(testdata["sleep_time"])

    post_title = site.find_element(
        "xpath", '//*[@id="app"]/main/div/div[1]/h1')
    assert post_title.text == "Здесь могла бы быть ваша реклама"
