import time

from Data import reading_object
bms_obj = reading_object.read_locators()


class OffersPage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_location(self):
        self.driver.find_element(*bms_obj['click_on_location']).click()
        # time.sleep(4)

    def click_on_offers(self):
        self.driver.find_element(*bms_obj["click_on_offers"]).click()
        # time.sleep(3)

    def search_by_name(self,offers_):
        self.driver.find_element(*bms_obj['search_by_name']).send_keys(offers_[0])

    def check_offer(self):
        self.driver.find_element(*bms_obj['check_offer']).click()
        time.sleep(3)
        self.driver.find_element(*bms_obj["click_on_offers"]).click()

    def click_on_creditcard(self):
        self.driver.find_element(*bms_obj["click_on_creditcard"]).click()
        time.sleep(2)

    def check_credit_offer(self):
        self.driver.find_element(*bms_obj["check_credit_offer"]).click()
        time.sleep(3)
        self.driver.find_element(*bms_obj["click_on_offers"]).click()
    def click_on_debitcard(self):
        self.driver.find_element(*bms_obj["click_on_debitcard"]).click()

    def check_debit_offer(self):
        self.driver.find_element(*bms_obj["check_debit_offer"]).click()
        time.sleep(3)
        self.driver.find_element(*bms_obj["click_on_offers"]).click()

    def click_on_wallet(self):
        self.driver.find_element(*bms_obj["click_on_wallet"]).click()

    def check_wallet_offer(self):
        self.driver.find_element(*bms_obj["check_wallet_offer"]).click()