# Imports
import pytest
import logging as logger
from demostore_automation.src.pages.HomePage import HomePage
from demostore_automation.src.pages.CartPage import CartPage
from demostore_automation.src.pages.Header import Header
from demostore_automation.src.generic_helpers.generic_coupon_helper import GenericCouponHelper


# Declare any fixture the test will need - A fixture is a way to set up and tear down test dependencies and resources
# In this case, the init_driver fixture is responsible for setting up the WebDriver used for browser automation
@pytest.mark.usefixtures("init_driver")

# Define the test class
class TestExpiredCouponMessage:

# Define the test methods within the class 
    @pytest.mark.tcid101 # Custom marker for identification purposes
    def test_verify_expired_coupon_message(self):
        """
        This test verifies that applying an expired coupon will show an
        error saying 'This coupon has expired.'
        
        :params:
        :return:
        """
        
        # print out logs
        logger.info("Testing expired coupon message")

        # Perform a series of test actions on the application:
        
        # go to home page
        home_page = HomePage(self.driver)
        home_page.go_to_home_page()

        # add item to cart
        home_page.click_first_add_to_cart_button()
        header = Header(self.driver)
        header.wait_until_cart_item_count(1)

        # go to cart
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart_page()

        # input expired coupon
        coupon_code = GenericCouponHelper().create_coupon(expired=True)
        cart_page.apply_coupon(coupon_code)
        
        # verify that the expired coupon message appears after coupon is applied
        displayed_err = cart_page.get_displayed_error()
        expected_err = 'This coupon is expired.'
        assert displayed_err == expected_err, f"After applying expired coupon, expected to see"\
                                              f"Error message '{expected_err}', but"\
                                              f"actual displayed is '{displayed_err}'."