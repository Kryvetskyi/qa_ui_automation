from pages.widget_page import AccordianPage


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
