from locators import TextBox

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestTextBox:

    def test_send_valid_text_box_form(self):
        browser = webdriver.Chrome()
        browser.get("https://demoqa.com/text-box")

        # отправляем валидные данные в форму
        name = "Bulochka s koricey"
        user_name_input = browser.find_element(*TextBox.USER_NAME_INPUT)
        user_name_input.send_keys(name)

        email = "test@test.ru"
        user_email_input = browser.find_element(*TextBox.USER_EMAIL_INPUT)
        user_email_input.send_keys(email)

        current_address = "Saint-Petersburg"
        current_address_input = browser.find_element(*TextBox.CURRENT_ADDRESS_INPUT)
        current_address_input.send_keys(current_address)

        permanent_address = "Moscow"
        permanent_address_input = browser.find_element(By.ID, "permanentAddress")
        permanent_address_input.send_keys(permanent_address)

        # нажимаем кнопку отправить
        submit_button = browser.find_element(*TextBox.SUBMIT_BUTTON)
        submit_button.click()

        # проверяем, вывелось ли наше имя. Если не вывелось - выводим ошибку и значение поля
        output_name = browser.find_element(*TextBox.OUTPUT_NAME)
        assert output_name.text == "Name:" + name, f"Name value is {output_name.text}"

        browser.quit()

    def test_send_invalid_email(self):
        browser = webdriver.Chrome()
        browser.get("https://demoqa.com/text-box")

        name = "Bulochka s koricey"
        user_name_input = browser.find_element(*TextBox.USER_NAME_INPUT)
        user_name_input.send_keys(name)

        # отправляем невалидную почту
        email = "test"
        user_email_input = browser.find_element(*TextBox.USER_EMAIL_INPUT)
        user_email_input.send_keys(email)

        current_address = "Saint-Petersburg"
        current_address_input = browser.find_element(*TextBox.CURRENT_ADDRESS_INPUT)
        current_address_input.send_keys(current_address)

        permanent_address = "Moscow"
        permanent_address_input = browser.find_element(By.ID, "permanentAddress")
        permanent_address_input.send_keys(permanent_address)

        # нажимаем кнопку отправить
        submit_button = browser.find_element(*TextBox.SUBMIT_BUTTON)
        submit_button.click()

        # проверяем, выделено ли поле ввода почты красным. Если нет - выводим цвет, которым выделено поле
        assert user_email_input.value_of_css_property("color") == "rgba(73, 80, 87, 1)", \
            f"Color value is {user_email_input.value_of_css_property('color')}"
        
        browser.quit()
