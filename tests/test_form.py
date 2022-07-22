import allure
from pages.form_page import FormPage


@allure.suite('Form')
class TestForm:

    @allure.feature('Test Form')
    class TestFormPage:

        @allure.title('Check form.')
        def test_form(self, driver, output_file):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            file_path, _ = output_file
            person = form_page.fill_form_page(file_path)
            modal_form = form_page.check_added_student()
            assert [f'{person.firstname} {person.lastname}', person.email, person.mobile] \
                   == [modal_form[0], modal_form[1], modal_form[3]]
