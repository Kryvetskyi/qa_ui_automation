import random
from generator.generator import generate_person
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FormPage(BasePage):
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']")
    MOBILE = (By.CSS_SELECTOR, "input[id='userNumber']")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    SUBJECT = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    HOBBIES = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1, 3)}']")
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    SELECT_STATE = (By.CSS_SELECTOR, "div[id='state']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    SELECT_CITY = (By.CSS_SELECTOR, "div[id='city']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    SUBMIT = (By.CSS_SELECTOR, "#submit")
    RESULT_MODAL_TABLE = (By.XPATH, "//div[@class='table-responsive']//td[2]")

    def fill_form_page(self, file_to_load):
        person_info = next(generate_person())
        self.remove_footer()
        self.is_element_visible(self.FIRSTNAME_INPUT).send_keys(person_info.firstname)
        self.is_element_visible(self.LASTNAME_INPUT).send_keys(person_info.lastname)
        self.is_element_visible(self.EMAIL).send_keys(person_info.email)
        self.is_element_visible(self.GENDER).click()
        self.is_element_visible(self.MOBILE).send_keys(person_info.mobile)
        self.is_element_visible(self.SUBJECT).send_keys('Math')
        self.is_element_visible(self.SUBJECT).send_keys(Keys.RETURN)
        self.is_element_visible(self.HOBBIES).click()
        self.is_element_present(self.UPLOAD_FILE).send_keys(file_to_load)
        self.is_element_visible(self.CURRENT_ADDRESS).send_keys(person_info.cur_addr)
        self.is_element_present(self.SELECT_STATE).click()
        self.is_element_present(self.STATE_INPUT).send_keys(Keys.RETURN)
        self.is_element_present(self.SELECT_CITY).click()
        self.is_element_present(self.CITY_INPUT).send_keys(Keys.RETURN)
        self.is_element_present(self.SUBMIT).click()
        return person_info

    def check_added_student(self):
        modal_window = self.are_elements_present(self.locators.RESULT_MODAL_TABLE)
        return [student.text for student in modal_window]
