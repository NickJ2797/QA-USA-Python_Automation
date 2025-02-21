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
        cls.driver.get(data.Urban_ROUTES_URL)
        if helpers.is_url_reachable(data.Urban_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
      urban_routes_page = UrbanRoutesPage(self.driver)
      urban_routes_page.enter_route(data.ADDRESS_FROM,data.ADDRESS_TO)
      assert urban_routes_page.get_from() == data.ADDRESS_FROM
      assert urban_routes_page.get_to() == data.ADDRESS_TO




    def test_select_plan(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_supportive_plan()


    def test_fill_phone_number(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.fill_phone_number()
        assert urban_routes_page.get_phone() == data.PHONE_NUMBER

    def test_fill_card(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.fill_phone_number()
        urban_routes_page.fill_card(data.CARD_NUMBER,data.CARD_CODE)
        assert urban_routes_page.get_card_number() == data.CARD_NUMBER
        assert urban_routes_page.get_card_code() == data.CARD_CODE


    def test_comment_for_driver(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)
        assert urban_routes_page.get_comment() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.order_blanket_and_handkerchiefs()
        assert urban_routes_page.is_switch_on() == True, "Switch was not toggled on!"

    def test_order_2_ice_creams(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.order_2_ice_creams()

    def test_car_search_model_appears(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.call_taxi()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)
        urban_routes_page.order_taxi_with_supportive_tariff()

    @classmethod
    def teardown_class(cls):
       cls.driver.quit()


