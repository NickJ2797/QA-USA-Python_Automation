
class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.Urban_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. CHeck the server is on and still running")
    def test_set_route(self):
        # Add in S8
        print("Function created for set route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("Function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("Function created for fill phone number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("Function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("Function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("Function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        #Test ordering two ice creams using the Urban Routes app.
     for _ in range(2):
        # Add in S8
        print("Function created for order 2 ice creams")
        pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("Function created for car search model appears")
        pass

import data
import helpers