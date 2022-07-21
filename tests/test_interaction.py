from typing import Type

from pages.base_page import BasePage
from pages.interactions_page import (
    SortablePage,
    SelectablePage,
    ResizablePage,
)


class TestInteractions:

    class TestSortable:
        def test_sorted_list(self, driver):
            sorted_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sorted_page.open()
            assert sorted_page.test_elements('list')
            assert sorted_page.test_elements('grid')

    class TestSelectable:
        def test_sorted_list(self, driver):

            selected_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selected_page.open()
            assert selected_page.test_elements('grid')
            assert selected_page.test_elements('list')

    class TestResizable:
        def test_resizable(self, driver):
            resize_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resize_page.open()
            assert resize_page.test_elements('resizable')
            assert resize_page.test_elements('resizable-box')
