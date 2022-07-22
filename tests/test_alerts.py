import allure
from pages.alerts_page import (
    BrowserWindowsPage,
    AlertPage,
    FramePage,
    NestedFrame,
    ModalDialog
)


@allure.suite
class TestAlertFrameWindow:

    @allure.feature('Test Browser Windows')
    class TestBrowserWindows:

        @allure.title('Check new tab.')
        def test_new_tab(self, driver):
            tab = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            tab.open()
            title = tab.check_tab_opened()
            assert title == 'This is a sample page', 'New tab was not open or title is not present.'

        @allure.title('Check new window.')
        def test_new_window(self, driver):
            window = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            window.open()
            title = window.check_tab_opened()
            assert title == 'This is a sample page', 'New tab was not open or title is not present.'

    @allure.feature('Test Alert')
    class TestAlert:

        @allure.title('Check see alert.')
        def test_check_see_alert(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button'

        @allure.title('Check alert appears.')
        def test_check_alert_appears(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appears()
            assert alert_text == 'This alert appeared after 5 seconds'

        @allure.title('Check confirm result.')
        def test_check_confirm_result(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok'

        @allure.title('Check confirm prompt.')
        def test_check_confirm_prompt(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text_to_send, result_text = alert_page.check_confirm_prompt()
            assert text_to_send in result_text

    @allure.feature('Test Frame')
    class TestFrame:

        @allure.title('Check frames.')
        def test_frames(self, driver):
            frame_page = FramePage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            first = frame_page.check_frame('frame1')
            second = frame_page.check_frame('frame2')
            assert first == ['500px', '350px', 'This is a sample page']
            assert second == ['100px', '100px', 'This is a sample page']

    @allure.feature('Test Nested Frames')
    class TestNestedFrames:

        @allure.title('Check nested frames.')
        def test_nested_frame(self, driver):
            nested_frame = NestedFrame(driver, 'https://demoqa.com/nestedframes')
            nested_frame.open()
            parent, child = nested_frame.check_nested_frame()
            assert parent == 'Parent frame'
            assert child == 'Child Iframe'

    @allure.feature('Test Modal Dialogs')
    class TestModalDialogs:

        @allure.title('Check modal dialogs.')
        def test_modal_dialogs(self, driver):
            modal_dialog = ModalDialog(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog.open()
            small, large = modal_dialog.check_modal_dialog()

            assert small[0] == 'Small Modal'
            assert large[0] == 'Large Modal'
            assert 'This is a small modal' in small[1]
            assert 'Lorem Ipsum' in large[1]
