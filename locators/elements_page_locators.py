from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEMS_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    ITEM_TITLE = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_IMPRESSIVE_RADIO = (By.CSS_SELECTOR, "label[for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class WebTablePageLocators:
    # Person Creation form
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # Persons table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_BOX = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class ='rt-tr-group']"
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "select[aria-label = 'rows per page']")


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, "//div[3]/button")
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    CLICK_ME_MESSAGE = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")


class LinksPageLocators:
    VALID_HOME_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    INVALID_LINK = (By.CSS_SELECTOR, "a[id='bad-request']")


class DownloadPageLocators:
    FILE_INPUT = (By.CSS_SELECTOR, "input[id='uploadFile']")
    FILE_TEXT = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "a[id='downloadButton']")


class DynamicPropertiesLocators:
    COLOR_CHANGE = (By.CSS_SELECTOR,  "button[id='colorChange']")
    ENABLE_BUTTON = (By.CSS_SELECTOR,  "button[id='enableAfter']")
    VISIBLE_AFTER = (By.CSS_SELECTOR,  "button[id='visibleAfter']")
