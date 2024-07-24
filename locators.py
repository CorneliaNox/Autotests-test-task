from selenium.webdriver.common.by import By

class TextBox:
    USER_NAME_INPUT = (By.ID, "userName")
    USER_EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    OUTPUT_NAME = (By.ID, "name")