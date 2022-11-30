from POM.offers_module import OffersPage
from Data import reading_object
import pytest

data_obj = reading_object.read_data()


@pytest.mark.parametrize("offers_",data_obj)
class TestOffers:
    def test_offers(self,_driver,offers_):
        op = OffersPage(_driver)

        op.click_on_location()
        op.click_on_offers()
        op.search_by_name(offers_)
        op.check_offer()
        op.click_on_creditcard()
        op.check_credit_offer()
        op.click_on_debitcard()
        op.check_debit_offer()
        op.click_on_wallet()
        op.check_wallet_offer()

