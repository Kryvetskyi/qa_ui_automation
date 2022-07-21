from pages.interactions_page import (
    SortablePage,
    SelectablePage,
    ResizablePage,
    DroppablePage,
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

    class TestDroppable:

        def test_drag_simple(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            assert droppable_page.drag_simple()

        def test_drag_acceptable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            assert droppable_page.drag_acceptable('not_accept') != 'Dropped!'
            assert droppable_page.drag_acceptable('accept') == 'Dropped!'

        def test_drag_prevent(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            assert 'Outer droppable' in droppable_page.drag_prevent()
