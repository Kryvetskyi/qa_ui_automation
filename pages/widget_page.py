import time
import random
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from generator.generator import generate_color
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import JavascriptException


class AccordianPage(BasePage):
    _FIRST_SECTION = (By.CSS_SELECTOR, "div[id='section1Heading']")
    _FIRST_SECTION_CONTENT = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    _SECOND_SECTION = (By.CSS_SELECTOR, "div[id='section2Heading']")
    _SECOND_SECTION_CONTENT = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    _THIRD_SECTION = (By.CSS_SELECTOR, "div[id='section3Heading']")
    _THIRD_SECTION_CONTENT = (By.CSS_SELECTOR, "div[id='section3Content'] p")

    def check_accordian(self, widget):
        try:
            self.remove_footer()
        except JavascriptException:
            pass
        widgets = {
            'first': {
                'title': self._FIRST_SECTION,
                'content': self._FIRST_SECTION_CONTENT},
            'second': {'title': self._SECOND_SECTION,
                       'content': self._SECOND_SECTION_CONTENT},
            'third': {'title': self._THIRD_SECTION,
                      'content': self._THIRD_SECTION_CONTENT}
        }

        widget_title = self.is_element_visible(widgets[widget]['title'])
        try:
            widget_content = self.is_element_visible(widgets[widget]['content']).text
        except TimeoutException:
            widget_title.click()
            widget_content = self.is_element_visible(widgets[widget]['content']).text

        return [widget_title.text, widget_content]


class AutoCompletePage(BasePage):
    _MULTIPLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    _MULTIPLE_VALUE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value']")
    _REMOVE_MULTIPLE_VALUE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path")
    _SINGLE_VALUE = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")
    _SINGLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")

    def fill_multi_input(self):
        colors_for_input = random.sample(next(generate_color()).color_name, k=random.randint(2, 4))
        for color in colors_for_input:
            color_input = self.is_element_clickable(self._MULTIPLE_INPUT)
            color_input.send_keys(color)
            time.sleep(0.1)
            color_input.send_keys(Keys.ENTER)
        colors_values = self.are_elements_present(self._MULTIPLE_VALUE)
        result_input = [color.text for color in colors_values]
        return colors_for_input, result_input

    def remove_color(self):
        colors_before = len(self.are_elements_visible(self._MULTIPLE_VALUE))
        remove_button_list = self.are_elements_visible(self._REMOVE_MULTIPLE_VALUE)
        for color in remove_button_list:
            color.click()
            break
        colors_after = len(self.are_elements_visible(self._MULTIPLE_VALUE))
        return colors_before, colors_after

    def fill_single_input(self):
        color = random.choice(next(generate_color()).color_name)
        color_input = self.is_element_visible(self._SINGLE_INPUT)
        color_input.send_keys(color)
        color_input.send_keys(Keys.ENTER)
        value = self.is_element_visible(self._SINGLE_VALUE).text
        return color, value



