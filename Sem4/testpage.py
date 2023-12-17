from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from zeep import Client, Settings


class TestSearchLocators:
    ids = dict()
    with open(r"E:\Учеба\Учусь\Automating Web Application Testing in Python\Sem4\locators.yaml") as f:
        locators = yaml.safe_load(f)

    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test form {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    def enter_login(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def enter_title_post(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_POST_TITLE"], word, description="password form")

    def enter_content_post(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_POST_CONTENT"], word, description="post content form")

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="error 401")

    def get_text_blog(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_RESULT_LOGIN"], description="result word blog")

    def click_login_button(self):
        self.click_button(
            TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login button")

    def click_create_new_post_button(self):
        self.click_button(
            TestSearchLocators.ids["LOCATOR_CREATE_POST_BTN"], description="button create new post")

    def click_new_post_button(self):
        self.click_button(
            TestSearchLocators.ids["LOCATOR_CREATE_NEW_POST"], description="button create new post")

    def post(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_POST"], description="result title of the post")

    def contact_us_form(self, name, email, content):
        logging.info("Filling out Contact Us form")

        self.click_button(
            TestSearchLocators.ids["LOCATOR_CONTACT_BUTTON"], description="click to contact")

        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_NAME_FIELD"], name, description="enter your name form")
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_EMAIL_FIELD"], email, description="enter your email form")
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_CONTENT_FIELD"], content, description="enter your content form")

        self.click_button(
            TestSearchLocators.ids["LOCATOR_SUBMIT_BUTTON"], description="click for sumbit")

        wait = WebDriverWait(self.driver, 3)
        alert = wait.until(EC.alert_is_present())

        alert_text = alert.text

        alert.accept()

        return alert_text

    def click_post_title_link(self):
        self.click_button(
            TestSearchLocators.ids["LOCATOR_POST_TITLE_LINK"], description="post title link")  # test 5

    def check_word(self, word):
        with open(r'E:\Учеба\Учусь\Automating Web Application Testing in Python\Sem4\testdata.yaml') as f:
            testdata = yaml.safe_load(f)

        url = testdata.get("url")
        settings = Settings(strict=False)
        client = Client(wsdl=url, settings=settings)
        return client.service.checkText(word)[0]['s']

    def get_text_from_h1(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_POST_TITLE_H1"], description="post title h1")
