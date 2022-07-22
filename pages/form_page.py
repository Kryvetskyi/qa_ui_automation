from generator.generator import generate_person
from selenium.webdriver import Keys
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_page(self, file_to_load):
        person_info = next(generate_person())
        self.remove_footer()
        self.is_element_visible(self.locators.FIRSTNAME_INPUT).send_keys(person_info.firstname)
        self.is_element_visible(self.locators.LASTNAME_INPUT).send_keys(person_info.lastname)
        self.is_element_visible(self.locators.EMAIL).send_keys(person_info.email)
        self.is_element_visible(self.locators.GENDER).click()
        self.is_element_visible(self.locators.MOBILE).send_keys(person_info.mobile)
        self.is_element_visible(self.locators.SUBJECT).send_keys('Math')
        self.is_element_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.is_element_visible(self.locators.HOBBIES).click()
        self.is_element_present(self.locators.UPLOAD_FILE).send_keys(file_to_load)
        self.is_element_visible(self.locators.CURRENT_ADDRESS).send_keys(person_info.cur_addr)
        self.is_element_present(self.locators.SELECT_STATE).click()
        self.is_element_present(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.is_element_present(self.locators.SELECT_CITY).click()
        self.is_element_present(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.is_element_present(self.locators.SUBMIT).click()
        return person_info

    def check_added_student(self):
        modal_window = self.are_elements_present(self.locators.RESULT_MODAL_TABLE)
        return [student.text for student in modal_window]
