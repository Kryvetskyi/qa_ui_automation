from pages.widget_page import (
    AccordianPage,
    AutoCompletePage,
    DateTimePage,
    SliderPage,
    ProgressBarPage
)


class TestWidget:
    class TestAccordingPage:

        def test_according_widgets(self, driver):
            according_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            according_page.open()
            first, first_content = according_page.check_accordian('first')
            second, second_content = according_page.check_accordian('second')
            third, third_content = according_page.check_accordian('third')

            assert first == 'What is Lorem Ipsum?' and len(first_content) > 0, 'Incorrect title or text body.'
            assert second == 'Where does it come from?' and len(second_content) > 0, 'Incorrect title or text body.'
            assert third == 'Why do we use it?' and len(third_content) > 0, 'Incorrect title or text body.'

    class TestAutoComplete:
        def test_autocomplete_color(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            colors_input, colors_input_result = auto_complete_page.fill_multi_input()

            assert colors_input == colors_input_result, 'Colors were not inputted or not presented.'

        def test_remove_color(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_multi_input()
            colors_before, colors_after = auto_complete_page.remove_color(), 'Color was not removed.'

            assert colors_before > colors_after

        def test_single_input(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color_for_input, result = auto_complete_page.fill_single_input()

            assert color_for_input == result, 'Color was not inputted or not presented.'

    class TestDateTime:
        def test_date(self, driver):
            date_time_page = DateTimePage(driver, 'https://demoqa.com/date-picker')
            date_time_page.open()
            date_before, date_after = date_time_page.select_date()

            assert date_before != date_after,'Date was not changed'

        def test_date_time(self, driver):
            date_time_page = DateTimePage(driver, 'https://demoqa.com/date-picker')
            date_time_page.open()
            date_time_page.select_date_and_time()
            date_before, date_after = date_time_page.select_date_and_time()
            assert date_before != date_after, 'Date was not changed'

    class TestSlider:
        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            value_before, value_after = slider_page.check_slider()
            assert value_before != value_after, 'Slider bar value was not changed'

    class TestProgressBar:
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            value_before, value_after = progress_bar_page.check_progress_bar()
            assert value_before != value_after, 'Progress bar value was not changed'
