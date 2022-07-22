from pages.interactions_page import (
    SortablePage,
    SelectablePage,
    ResizablePage,
    DroppablePage,
)
import allure


@allure.suite('Interactions.')
class TestInteractions:

    @allure.feature('Test Sortable.')
    class TestSortable:

        @allure.title('Check sorted list and grid.')
        def test_sorted_list(self, driver):
            sorted_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sorted_page.open()
            assert sorted_page.test_elements('list')
            assert sorted_page.test_elements('grid')

    @allure.feature('Test Selectable.')
    class TestSelectable:

        @allure.title('Check selected list and grid.')
        def test_sorted_list(self, driver):
            selected_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selected_page.open()
            assert selected_page.test_elements('grid')
            assert selected_page.test_elements('list')

    @allure.feature('Test Resizeable.')
    class TestResizable:

        @allure.title('Check resizable boxes.')
        def test_resizable(self, driver):
            resize_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resize_page.open()
            assert resize_page.test_elements('resizable')
            assert resize_page.test_elements('resizable-box')

    @allure.feature('Test Droppable.')
    class TestDroppable:

        @allure.title('Check drag and drop simple.')
        def test_drag_simple(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            assert droppable_page.drag_simple()

        @allure.title('Check drag and drop acceptable.')
        def test_drag_acceptable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            assert droppable_page.drag_acceptable('not_accept') != 'Dropped!'
            assert droppable_page.drag_acceptable('accept') == 'Dropped!'

        @allure.title('Check drag and drop prevent.')
        def test_drag_prevent(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            assert 'Outer droppable' in droppable_page.drag_prevent()
