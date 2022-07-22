import random
import time
import requests
import base64
import os
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from generator.generator import generate_person
from pages.base_page import BasePage


class TestBoxPage(BasePage):
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

    def fill_all_fields(self):
        person_info = next(generate_person())
        full_name = person_info.full_name
        email = person_info.email
        current_addr = person_info.cur_addr.replace('\n', '')
        permanent_addr = person_info.permanent_addr.replace('\n', '')

        self.is_element_visible(self.FULL_NAME).send_keys(full_name)
        self.is_element_visible(self.EMAIL).send_keys(email)
        self.is_element_visible(self.CURRENT_ADDRESS).send_keys(current_addr)
        self.is_element_visible(self.PERMANENT_ADDRESS).send_keys(permanent_addr)
        self.scroll_down()
        self.is_element_visible(self.SUBMIT).click()

        return full_name, email, current_addr, permanent_addr

    def check_filled_form(self):
        full_name = self.is_element_present(self.CREATED_FULL_NAME).text.split(':')[1]
        email = self.is_element_present(self.CREATED_EMAIL).text.split(':')[1]
        current_addr = self.is_element_present(self.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_addr = self.is_element_present(self.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_addr, permanent_addr


class CheckBoxPage(BasePage):
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEMS_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    ITEM_TITLE = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")

    def open_full_list(self):
        self.is_element_visible(self.EXPAND_ALL_BUTTON).click()

    def click_random_check_box(self):
        items_list = self.are_elements_visible(self.ITEMS_LIST)

        count = 23
        while count != 0:
            item = items_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_items(self):
        checked_items = self.are_elements_present(self.CHECKED_ITEMS)
        data = []
        for box in checked_items:
            item_title = box.find_element("xpath", self.ITEM_TITLE)
            data.append(item_title.text)
        return str(data).lower().replace('.doc', '').replace(' ', '')

    def get_success_text_output(self):
        result_list = self.are_elements_present(self.OUTPUT_RESULT)
        items_text = [word.text for word in result_list]
        return str(items_text).lower().replace(' ', '')


class RadioButtonPage(BasePage):
    YES_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_IMPRESSIVE_RADIO = (By.CSS_SELECTOR, "label[for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")

    def click_radio_button(self, choice):
        choices = {
            "yes": self.YES_RADIO_BUTTON,
            "impressive": self.IMPRESSIVE_RADIO_BUTTON,
            "no": self.NO_IMPRESSIVE_RADIO
        }

        self.is_element_visible(choices[choice]).click()

    def get_success_text_output_from_radio_button(self):
        return self.is_element_visible(self.OUTPUT_RESULT)


class WebTablePage(BasePage):
    # Person Creation form
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # Persons table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_BOX = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class ='rt-tr-group']"
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "select[aria-label = 'rows per page']")

    def add_new_person(self, count=1):

        while count != 0:
            # Generate person info
            person_info = next(generate_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            # Click add button and fill all fields
            self.is_element_visible(self.ADD_BUTTON).click()
            self.is_element_visible(self.FIRSTNAME_INPUT).send_keys(firstname)
            self.is_element_visible(self.LASTNAME_INPUT).send_keys(lastname)
            self.is_element_visible(self.EMAIL_INPUT).send_keys(email)
            self.is_element_visible(self.AGE_INPUT).send_keys(age)
            self.is_element_visible(self.SALARY_INPUT).send_keys(salary)
            self.is_element_visible(self.DEPARTMENT_INPUT).send_keys(department)
            self.is_element_visible(self.SUBMIT).click()
            count -= 1

            return [firstname, lastname, str(age), email, str(salary), department]

    def check_added_person(self):
        persons_list = self.are_elements_present(self.FULL_PEOPLE_LIST)
        return [person.text.splitlines() for person in persons_list]

    def search_some_person(self, person_data):
        self.is_element_visible(self.SEARCH_BOX).send_keys(person_data)

    def check_searched_person(self):
        delete_button = self.is_element_visible(self.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generate_person())
        age = person_info.age
        self.is_element_visible(self.UPDATE_BUTTON).click()
        self.is_element_visible(self.AGE_INPUT).clear()
        self.is_element_visible(self.AGE_INPUT).send_keys(age)
        self.is_element_visible(self.SUBMIT).click()
        return str(age)

    def delete_person(self):
        return self.is_element_visible(self.DELETE_BUTTON).click()

    def check_deleted(self):
        return self.is_element_visible(self.NO_ROWS_FOUND).text

    def select_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for row in count:
            self.scroll_down()
            self.is_element_visible(self.COUNT_ROW_LIST).click()
            self.is_element_visible(By.CSS_SELECTOR, f"option[value='{row}']").click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        return len(self.are_elements_present(self.FULL_PEOPLE_LIST))


class ButtonsPage(BasePage):
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, "//div[3]/button")
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    CLICK_ME_MESSAGE = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")

    def click_different_buttons(self):
        self.action_double_click(self.is_element_visible(self.DOUBLE_CLICK_BUTTON))
        self.action_right_click(self.is_element_visible(self.RIGHT_CLICK_BUTTON))
        self.is_element_visible(self.CLICK_ME_BUTTON).click()

    def check_buttons_text(self):
        first = self.is_element_visible(self.DOUBLE_CLICK_MESSAGE).text
        second = self.is_element_visible(self.RIGHT_CLICK_MESSAGE).text
        last = self.is_element_visible(self.CLICK_ME_MESSAGE).text
        return first, second, last


class LinksPage(BasePage):
    VALID_HOME_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    INVALID_LINK = (By.CSS_SELECTOR, "a[id='bad-request']")

    def check_new_tab_valid_link(self):
        valid_link = self.is_element_visible(self.VALID_HOME_LINK)
        link_href = valid_link.get_attribute('href')
        response = requests.get(f'{link_href}bad')
        if response.status_code == 200:
            valid_link.click()
            self.switch_to_new_tab()
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, f'Status code: {response.status_code}'

    def check_broken_link(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            return self.is_element_visible(self.INVALID_LINK)
        else:
            return r.status_code


class DownloadPage(BasePage):
    FILE_INPUT = (By.CSS_SELECTOR, "input[id='uploadFile']")
    FILE_TEXT = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "a[id='downloadButton']")

    def upload_file(self, file):
        return self.is_element_present(self.FILE_INPUT).send_keys(file)

    def get_uploaded_file_text(self):
        return self.is_element_visible(self.FILE_TEXT).text.split('\\')[-1]

    def download_file(self, file_path):
        link = self.is_element_present(self.DOWNLOAD_BUTTON).get_attribute('href')
        link = base64.b64decode(link)
        offset = link.find(b'\xff\xd8')

        with open(file_path, 'wb') as f:
            f.write(link[offset:])
            check_file = os.path.exists(file_path)
        return check_file


class DynamicProperties(BasePage):
    COLOR_CHANGE = (By.CSS_SELECTOR, "button[id='colorChange']")
    ENABLE_BUTTON = (By.CSS_SELECTOR, "button[id='enableAfter']")
    VISIBLE_AFTER = (By.CSS_SELECTOR, "button[id='visibleAfter']")

    def check_button_enabled(self):
        try:
            self.is_element_clickable(self.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

    def check_changed_color(self):
        color_button = self.is_element_present(self.COLOR_CHANGE)
        color_before = color_button.value_of_css_property('color')
        color_button.click()
        time.sleep(5)
        color_after = color_button.value_of_css_property('color')
        return color_before, color_after

    def check_button_appears(self):
        try:
            self.is_element_visible(self.VISIBLE_AFTER)
        except TimeoutException:
            return False
        return True
