from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    route_input_locator = (By.ID, 'route-input')
    submit_button_locator = (By.ID, 'submit-button')
    plan_selector_locator = (By.ID, 'plan-selector')
    phone_number_input_locator = (By.ID, 'phone-number-input')
    phone_code_input_locator = (By.ID, 'phone-code-input')
    card_input_locator = (By.ID, 'card-input')
    card_cvv_locator = (By.CLASS_NAME, 'card-cvv-input')
    link_button_locator = (By.ID, 'link-button')
    comment_input_locator = (By.ID, 'comment-input')
    blanket_option_locator = (By.ID, 'blanket-option')
    handkerchief_option_locator = (By.ID, 'handkerchief-option')
    blanket_assert_locator = (By.ID, 'blanket-assert')
    handkerchief_assert_locator = (By.ID, 'handkerchief-assert')
    ice_cream_option_locator = (By.ID, 'ice-cream-option')
    car_search_input_locator = (By.ID, 'car-search-input')
    supportive_plan_locator = (By.XPATH, "//option[@value='Supportive']")
    driver_message_locator = (By.ID, 'driver-message')
    order_button_locator = (By.ID, 'order-button')
    car_search_modal_locator = (By.ID, 'car-search-modal')

    # Methods
    def set_route(self, route):
        route_input = self.driver.find_element(*self.route_input_locator)
        route_input.clear()
        route_input.send_keys(route)

    def submit_route(self):
        submit_button = self.driver.find_element(*self.submit_button_locator)
        submit_button.click()

    def select_supportive_plan(self):
        plan_selector = self.driver.find_element(*self.plan_selector_locator)
        plan_selector.click()
        supportive_plan = self.driver.find_element(*self.supportive_plan_locator)
        if not supportive_plan.is_selected():
            supportive_plan.click()

    def fill_phone_number(self, phone_number, helpers):
        phone_number_input = self.driver.find_element(*self.phone_number_input_locator)
        phone_number_input.clear()
        phone_number_input.send_keys(phone_number)
        phone_code = helpers.retrieve_phone_code(phone_number)
        phone_code_input = self.driver.find_element(*self.phone_code_input_locator)
        phone_code_input.clear()
        phone_code_input.send_keys(phone_code)

    def fill_card(self, card_details, cvv):
        card_input = self.driver.find_element(*self.card_input_locator)
        card_input.clear()
        card_input.send_keys(card_details)
        card_cvv = self.driver.find_element(*self.card_cvv_locator)
        card_cvv.clear()
        card_cvv.send_keys(cvv)
        card_cvv.send_keys(Keys.TAB)
        link_button = self.driver.find_element(*self.link_button_locator)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(link_button))
        link_button.click()

    def comment_for_driver(self, comment):
        comment_input = self.driver.find_element(*self.comment_input_locator)
        comment_input.clear()
        comment_input.send_keys(comment)

    def order_blanket_and_handkerchiefs(self):
        blanket_option = self.driver.find_element(*self.blanket_option_locator)
        blanket_option.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.blanket_assert_locator)
        )
        handkerchief_option = self.driver.find_element(*self.handkerchief_option_locator)
        handkerchief_option.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.handkerchief_assert_locator)
        )

    def order_2_ice_creams(self):
        for _ in range(2):
            ice_cream_option = self.driver.find_element(*self.ice_cream_option_locator)
            ice_cream_option.click()

    def car_search_model_appears(self, model):
        car_search_input = self.driver.find_element(*self.car_search_input_locator)
        car_search_input.clear()
        car_search_input.send_keys(model)

    def order_taxi_with_supportive_tariff(self, message):
        self.select_supportive_plan()
        driver_message_input = self.driver.find_element(*self.driver_message_locator)
        driver_message_input.clear()
        driver_message_input.send_keys(message)
        order_button = self.driver.find_element(*self.order_button_locator)
        order_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.car_search_modal_locator)
        )


