
import time
import random
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from generator.generator import generate_color, generate_date
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


class DateTimePage(BasePage):
    _DATE_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    _DATE_SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    _DATE_SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    _DATE_SELECT_DAY = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

    _DATE_AND_TME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    _DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    _DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    _DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")
    _DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
    _DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")

    def select_date(self):
        date = next(generate_date())
        input_date = self.is_element_visible(self._DATE_INPUT)
        date_before = input_date.get_attribute('value')
        input_date.click()
        self.select_date_by_text(self._DATE_SELECT_MONTH, date.month)
        self.select_date_by_text(self._DATE_SELECT_YEAR, date.year)
        self.select_date_from_list(self._DATE_SELECT_DAY, date.day)
        date_after = input_date.get_attribute('value')

        return date_before, date_after

    def select_date_and_time(self):
        date = next(generate_date())
        input_date = self.is_element_visible(self._DATE_AND_TME_INPUT)
        date_before = input_date.get_attribute('value')
        input_date.click()
        self.scroll_down()

        # select month
        self.is_element_clickable(self._DATE_AND_TIME_MONTH).click()
        self.select_date_from_list(self._DATE_AND_TIME_MONTH_LIST, date.month)

        # select year
        self.is_element_clickable(self._DATE_AND_TIME_YEAR).click()
        self.select_date_from_list(self._DATE_AND_TIME_YEAR_LIST, str(random.randint(2018, 2027)))

        # select day
        self.select_date_from_list(self._DATE_SELECT_DAY, date.day)

        # select time
        self.select_date_from_list(self._DATE_AND_TIME_TIME_LIST, date.time)

        input_after = self.is_element_visible(self._DATE_AND_TME_INPUT)
        date_after = input_after.get_attribute('value')
        return date_before, date_after


class SliderPage(BasePage):
    _SLIDER_INPUT = (By.CSS_SELECTOR, "input[class*='range-slider range-slider--primary']")
    _SLIDER_VALUE = (By.CSS_SELECTOR, "input[id='sliderValue']")

    def check_slider(self):
        value_before = self.is_element_visible(self._SLIDER_VALUE).get_attribute('value')
        num = random.randint(1, 100)
        slider_input = self.is_element_visible(self._SLIDER_INPUT)
        self.drag_and_drop_by_offset(slider_input, num,  value_before)
        value_after = self.is_element_visible(self._SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    _SLIDER_BUTTON = (By.CSS_SELECTOR, "button[id='startStopButton']")
    _SLIDER_VALUE = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")

    def check_progress_bar(self):
        value_before = self.is_element_present(self._SLIDER_VALUE).text
        if value_before == '':
            value_before = 0
        self.is_element_visible(self._SLIDER_BUTTON).click()
        time.sleep(random.randint(1, 8))
        self.is_element_visible(self._SLIDER_BUTTON).click()
        value_after = self.is_element_present(self._SLIDER_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):
    _TAB_WHAT = (By.CSS_SELECTOR, "a[id='demo-tab-what']")
    _WHAT_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-what']")
    _TAB_ORIGIN = (By.CSS_SELECTOR, "a[id='demo-tab-origin']")
    _ORIGIN_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-origin']")
    _TAB_USE = (By.CSS_SELECTOR, "a[id='demo-tab-use']")
    _USE_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-use']")
    _TAB_MORE = (By.CSS_SELECTOR, "a[id='demo-tab-more']")
    _MORE_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-more']")

    def check_tabs(self):
        what = self.is_element_visible(self._WHAT_CONTENT).text
        self.is_element_visible(self._TAB_ORIGIN).click()
        origin = self.is_element_visible(self._ORIGIN_CONTENT).text
        self.is_element_visible(self._TAB_USE).click()
        use = self.is_element_visible(self._USE_CONTENT).text

        return what, origin, use


class ToolTipPage(BasePage):
    _TOOL_TIP_BUTTON = (By.CSS_SELECTOR, "button[id='toolTipButton']")
    _TOOL_TIPS_TEXT = (By.CSS_SELECTOR, "div[class='tooltip-inner']")
    _TOOL_TIP_INPUT = (By.CSS_SELECTOR, "input[id='toolTipTextField']")
    _TOOL_TIP_CONTRARY = (By.XPATH, "//*[.='Contrary']")
    _TOOL_TIP_1_10_32 = (By.XPATH, "//*[.='1.10.32']")

    def hover_button(self):
        self.move_to_element(self.is_element_visible(self._TOOL_TIP_BUTTON))
        return self.is_element_visible(self._TOOL_TIPS_TEXT).text

    def hover_input(self):
        self.move_to_element(self._TOOL_TIP_INPUT)
        return self.is_element_visible(self._TOOL_TIPS_TEXT).text

    def hover_contrary(self):
        self.move_to_element(self.is_element_visible(self._TOOL_TIP_CONTRARY))
        return self.is_element_visible(self._TOOL_TIPS_TEXT).text

    def hover_1_10_32_text(self):
        self.remove_footer()
        self.move_to_element(self.is_element_visible(self._TOOL_TIP_1_10_32))
        return self.is_element_visible(self._TOOL_TIPS_TEXT).text


class MenuPage(BasePage):
    _MENU_ITEMS = (By.CSS_SELECTOR, "ul[id='nav'] li a")

    def check_menu(self):
        items_list = self.are_elements_present(self._MENU_ITEMS)
        data = []
        for item in items_list:
            self.move_to_element(item)
            data.append(item.text)
        return data
