from selenium.webdriver.common.by import By

import data
import helpers
import time


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        # Define locators

        # set route
        self.route_input_from = (By.ID, 'from')
        self.route_input_to = (By.ID, 'to')
        self.call_taxi_locator = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
        #set route

        # enter phone number
        self.phone_number_click = (By.CSS_SELECTOR, 'div.np-button')
        self.phone_number_input_locator = (By.CSS_SELECTOR, 'input#phone.input')
        self.next_button =(By.XPATH, '//button[contains(text(), "Next")]')
        self.phone_code_input_locator = (By.CSS_SELECTOR, 'input#code.input')
        self.confirm_code_locator = (By.XPATH,'//button[contains(text(), "Confirm")]')
        # enter phone number

        #put in card info
        self.payment_method_locator = (By.XPATH, '//div[@class="pp-button filled"]//div[contains(text(), "Payment method")]')
        self.card_input_locator = (By.XPATH, '//div[contains(text(), "Add card")]')
        self.card_number_locator =(By.ID, 'number')
        self.payment_method_select = (By.XPATH, '//div[@class="pp-button filled"]//div[contains(text(), "Payment method")]')
        self.add_card_control = (By.XPATH, '//div[contains(text(), "Add card")]')
        self.card_number_input = (By.ID, 'number')
        self.card_code_input = (By.XPATH, '//input[@class="card-input" and @id="code"]')
        self.link_button_locator = (By.XPATH, '//button[contains(text(), "Link")]')
        # put in card info

        #comment for driver
        self.comment_input_locator = (By.XPATH, "//input[@id='comment']")
        #comment for driver

        #blanket
        self.order_requirement= (By.XPATH, '//div[contains (text(), "Order requirements")]')
        self.option_switches = (By.CLASS_NAME, 'switch')
        self.option_switches_assert = (By.CLASS_NAME, "switch-input")
        #blanket

        # ice cream
        self.ice_cream_option_locator = (By.XPATH, '//div[@class="r-counter-label" and contains(text(), "Ice cream")]')

        # order supportive car
        self.supportive_plan_locator = (By.XPATH, '//div[contains(text(), "Supportive")]//..')
        self.order_button_locator = (By.CLASS_NAME, 'smart-button-wrapper')

    def enter_from_route(self, from_text):
        # Enter From
        self.driver.find_element(*self.route_input_from).send_keys(from_text)
    def get_from(self):
        return self.driver.find_element(*self.route_input_from).get_property('value')


    def enter_to_route(self, to_text):
        # Enter To
        self.driver.find_element(*self.route_input_to).send_keys(to_text)
    def get_to(self):
        return self.driver.find_element(*self.route_input_to).get_property('value')


    def call_taxi(self):
        # Call taxi
        call_taxi_button = self.driver.find_element(*self.call_taxi_locator)
        call_taxi_button.click()

    def select_supportive_plan(self):
        #supportive button
        supportive_plan_button = self.driver.find_element(*self.supportive_plan_locator)
        if not supportive_plan_button.is_selected():
            supportive_plan_button.click()



    def fill_phone_number(self):
        phone_number_input = self.driver.find_element(*self.phone_number_input_locator)
        phone_number_c = self.driver.find_element(*self.phone_number_click)
        phone_number_c.click()
        phone_number_input.clear()  # Clear any pre-filled text
        phone_number_input.send_keys(data.PHONE_NUMBER)

        next_button = self.driver.find_element(*self.next_button)
        next_button.click()

        # Retrieve the phone code using the helper function
        phone_code = helpers.retrieve_phone_code(self.driver)

        phone_code_input = self.driver.find_element(*self.phone_code_input_locator)
        phone_code_input.clear()  # Clear any pre-filled text
        phone_code_input.send_keys(phone_code)

        confirm_button = self.driver.find_element(*self.confirm_code_locator)
        confirm_button.click()
    def get_phone(self):
        return self.driver.find_element(*self.phone_number_input_locator).get_property('value')



    def fill_card(self, card_details, cvv):
        self.driver.find_element(*self.payment_method_select).click()
        """this method sometimes gives error even with waits. In extreme case add
                time.sleep(2) """
        self.driver.find_element(*self.add_card_control).click()
        self.driver.find_element(*self.card_number_input).send_keys(card_details)
        self.driver.find_element(*self.card_code_input).send_keys(cvv)
        self.driver.find_element(*self.link_button_locator).click()

    def get_card_number(self):
        return self.driver.find_element(*self.card_number_input).get_property('value')
    def get_card_code(self):
        return self.driver.find_element(*self.card_code_input).get_property('value')


    def comment_for_driver(self, comment):
        self.driver.find_element(*self.comment_input_locator).send_keys(comment)
    def get_comment(self):
        return self.driver.find_element(*self.comment_input_locator).get_property('value')

    def order_blanket_and_handkerchiefs(self):
        switches = self.driver.find_elements(*self.option_switches)
        switch_assert = self.driver.find_elements(*self.option_switches_assert)
        time.sleep(3)
        switches[0].click()
    def is_switch_on(self):
        return self.driver.find_element(*self.option_switches_assert).is_selected()



    def order_2_ice_creams(self):
        for _ in range(2):
           self.driver.find_element(*self.ice_cream_option_locator).click()


    def order_taxi_with_supportive_tariff(self):
        self.driver.find_element(*self.order_button_locator).click()
        time.sleep(38)


    #Step to enter both "from" and "to" locations
    def enter_route(self, from_text, to_text):
        self.enter_from_route(from_text)
        self.enter_to_route(to_text)

