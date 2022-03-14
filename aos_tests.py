import unittest
import aos_locators as locators
import aos_method as method

class aosAppPostiveTestCases(unittest.TestCase):

    @staticmethod   # single to units test that this is a static method
    def test_create():
        method.setup()
        method.create_new_user()
        method.log_out()
        method.log_in()
        method.homepage_texts()
        method.top_menu()
        method.contact_us_form()
        method.tearDown()