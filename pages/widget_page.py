from selenium.webdriver.common.by import By
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

