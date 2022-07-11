from pages.widget_page import AccordianPage, AutoCompletePage


class TestWidget:
    class TestAccordingPage:

        def test_according_widgets(self, driver):
            according_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            according_page.open()
            first, first_content = according_page.check_accordian('first')
            second, second_content = according_page.check_accordian('second')
            third, third_content = according_page.check_accordian('third')

            assert first == 'What is Lorem Ipsum?' and len(first_content) > 0
            assert second == 'Where does it come from?' and len(second_content) > 0
            assert third == 'Why do we use it?' and len(third_content) > 0

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
