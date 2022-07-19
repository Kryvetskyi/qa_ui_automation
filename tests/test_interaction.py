from pages.interactions_page import (
    SortablePage,
    SelectablePage,
)


class TestInteractions:

    class TestSortable:
        def test_sorted_list(self, driver):
            sorted_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sorted_page.open()
            list_before, list_after = sorted_page.check_if_elements_changed('list')
            grid, grid_after = sorted_page.check_if_elements_changed('grid')
            assert list_before != list_after
            assert grid != grid_after

    class TestSelectable:
        def test_sorted_list(self, driver):
            selected_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selected_page.open()
            grid_element = selected_page.check_selectable('grid')
            list_element = selected_page.check_selectable('list')
            assert grid_element is not None
            assert list_element is not None


