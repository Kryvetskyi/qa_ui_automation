import random
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class SortablePage(BasePage):
    _LIST_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    _GRID_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    _LIST_ITEMS = (By.CSS_SELECTOR, "div[id='demo-tabpane-list'] div[class='list-group-item list-group-item-action']")
    _GRID_ITEMS = (By.CSS_SELECTOR, "div[id='demo-tabpane-grid'] div[class='list-group-item list-group-item-action']")

    config = {
        'list': (_LIST_TAB, _LIST_ITEMS),
        'grid': (_GRID_TAB, _GRID_ITEMS)
    }

    def get_elements_and_text(self, tab_type: str, tab_items: WebElement) -> tuple:
        """Get elements for other function and text from elements for test."""
        self.is_element_visible(tab_type).click()
        elements = random.sample(self.are_elements_visible(tab_items), k=2)
        elements_text = [item.text for item in elements]
        return elements, elements_text

    def change_random_position(self, elements: list[WebElement]) -> None:
        element_to_change = elements[0]
        where_to_put_element = elements[1]
        self.drag_and_drop_to_element(element_to_change, where_to_put_element)

    def test_elements(self, interaction_type: str) -> bool:
        tab_type, tab_items = self.config[interaction_type]
        elements, items_before = self.get_elements_and_text(tab_type, tab_items)
        self.change_random_position(elements)
        _, items_after = self.get_elements_and_text(tab_type, tab_items)
        return items_before != items_after


class SelectablePage(BasePage):
    _LIST_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    _NOT_ACTIVE_LIST_ITEMS = (By.CSS_SELECTOR,
                              "div[id='demo-tabpane-list'] li[class='mt-2 list-group-item list-group-item-action']")
    _ACTIVE_LIST_ITEM = (By.CSS_SELECTOR,
                         "div[id='demo-tabpane-list'] li[class='mt-2 list-group-item active list-group-item-action']")

    _GRID_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    _NOT_ACTIVE_GRID_ITEMS = (By.CSS_SELECTOR,
                              "div[id='demo-tabpane-grid'] li[class='list-group-item list-group-item-action']")
    _ACTIVE_GRID_ITEM = (By.CSS_SELECTOR,
                         "div[id='demo-tabpane-grid'] li[class='list-group-item active list-group-item-action']")

    config = {
        'list': (_LIST_TAB, _NOT_ACTIVE_LIST_ITEMS, _ACTIVE_LIST_ITEM),
        'grid': (_GRID_TAB, _NOT_ACTIVE_GRID_ITEMS, _ACTIVE_GRID_ITEM)
    }

    def get_elements(self, tab_type: str, tab_items: WebElement) -> list[WebElement]:
        """Get all elements."""
        self.is_element_visible(tab_type).click()
        elements = self.are_elements_visible(tab_items)
        return elements

    @staticmethod
    def click_random_item(elements: list[WebElement]) -> None:
        random.sample(elements, k=1)[0].click()

    def test_elements(self, interaction_type: str) -> bool:
        tab_type, tab_items, active_item = self.config[interaction_type]
        elements = self.get_elements(tab_type, tab_items)
        self.click_random_item(elements)
        return self.is_element_visible(active_item)


class ResizablePage(BasePage):
    _RESIZABLE = (By.CSS_SELECTOR, "div[id='resizable']")
    _RESIZABLE_BOX = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")
    _RESIZABLE_HANDLE = (By.CSS_SELECTOR,
                         "div[id='resizable'] span[class='react-resizable-handle react-resizable-handle-se']")
    _RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction'] \
        span[class='react-resizable-handle react-resizable-handle-se']")

    options = {
        'resizable': (_RESIZABLE, _RESIZABLE_HANDLE),
        'resizable-box': (_RESIZABLE_BOX, _RESIZABLE_BOX_HANDLE)
    }

    @staticmethod
    def get_width_height(value):
        width = value.split(';')[0].split(':')[1].strip()
        height = value.split(';')[1].split(':')[1].strip()
        return width, height

    def get_min_max_size(self, element):
        size = self.is_element_present(element)
        return size.get_attribute('style')

    def test_elements(self, box_type: str) -> bool:
        box, box_item = self.options[box_type]

        self.drag_and_drop_by_offset(self.is_element_present(box_item), 400, 200)
        max_size = self.get_width_height(self.get_min_max_size(box))

        self.drag_and_drop_by_offset(self.is_element_present(box_item), -400, -200)
        min_size = self.get_width_height(self.get_min_max_size(box))

        return max_size != min_size
