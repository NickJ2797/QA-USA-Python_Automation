from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from pages import UrbanRoutesPage
import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
      self.driver.get(data.URBAN_ROUTES_URL)
      urban_routes_page = UrbanRoutesPage(self.driver)
      urban_routes_page.enter_route(data.ADDRESS_FROM,data.ADDRESS_TO)
      assert urban_routes_page.get_from() == data.ADDRESS_FROM
      assert urban_routes_page.get_to() == data.ADDRESS_TO




    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_supportive_plan()
        assert urban_routes_page.get_selected_plan() == 'Supportive'


    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_supportive_plan()
        phone_number = data.PHONE_NUMBER
        urban_routes_page.fill_phone_number(phone_number)
        assert urban_routes_page.get_phone() == phone_number

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)
        urban_routes_page.fill_card(data.CARD_NUMBER,data.CARD_CODE)
        assert urban_routes_page.get_card_number() == data.CARD_NUMBER
        assert urban_routes_page.get_card_code() == data.CARD_CODE


    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)
        assert urban_routes_page.get_comment() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.order_blanket_and_handkerchiefs()
        assert urban_routes_page.is_switch_on() == True, "Switch was not toggled on!"

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.order_2_ice_creams()
        assert urban_routes_page.get_total_icecreams() == '2'

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)
        urban_routes_page.order_taxi_with_supportive_tariff()
        assert 'The driver will arrive' in urban_routes_page.get_supportive_tariff(), \
            f"Expected text 'The driver will arrive' not found in: {urban_routes_page.get_supportive_tariff()}"

    @classmethod
    def teardown_class(cls):
       cls.driver.quit()


