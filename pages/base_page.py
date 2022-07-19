from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def is_element_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def are_elements_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def is_element_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def are_elements_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def is_element_invisible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def is_element_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element).perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    def drag_and_drop_by_offset(self, element, position_x, position_y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, position_x, position_y).perform()

    def drag_and_drop_to_element(self, which, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(which, where).perform()

    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('close-fixedban').remove();")
        self.driver.execute_script("document.getElementsByTagName('iframe')[0].remove();")

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def select_date_by_text(self, element, value):
        select = Select(self.is_element_visible(element))
        select.select_by_visible_text(value)

    def select_date_from_list(self, elements, value):
        dates = self.are_elements_present(elements)
        for date in dates:
            if date.text == value:
                date.click()
                break

