import logging
import yaml
import time
from testpage import OperationsHelper
from testpage import TestSearchLocators

with open(r"E:\Учеба\Учусь\Automating Web Application Testing in Python\Sem4\testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test2 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()

    assert testpage.get_text_blog() == "Blog"


def test_step3(browser):
    logging.info("Test3 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()

    testpage.click_new_post_button()
    testpage.enter_title_post("new title")
    testpage.enter_content_post("content")
    testpage.click_create_new_post_button()

    time.sleep(3)

    assert testpage.post() == "new title"


def test_step4(browser):
    logging.info("Test4 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    time.sleep(testdata["sleep_time"])

    alert_text = testpage.contact_us_form(
        "Dmitriy", "dmitriy@ya.ru", "вот это - контент")

    expected_text = "Form successfully submitted"
    assert alert_text == expected_text, f"Текст алерта не совпадает. Ожидаемый: {expected_text}, Фактический: {alert_text}"


def test_step5(browser, good_word, bad_word, send_email):
    logging.info("Test5 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    time.sleep(testdata["sleep_time"])

    # Получение информации о данных из h1
    post_title = testpage.get_text_from_h1()

    if post_title:
        logging.info(f"Post title (h1): {post_title}")

        # Проверка хорошего или плохого слова
        assert good_word in testpage.check_word(
            bad_word), "Слово не является хорошим словом"
    else:
        logging.error("Post title (h1) element not found")
        assert False, "Элемент с данными (h1) не найден"
