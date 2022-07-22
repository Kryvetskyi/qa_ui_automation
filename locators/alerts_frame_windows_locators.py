from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    TAB = (By.CSS_SELECTOR, "button[id='tabButton']")
    WINDOW = (By.CSS_SELECTOR, "button[id='windowButton']")
    NEW_TAB = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
