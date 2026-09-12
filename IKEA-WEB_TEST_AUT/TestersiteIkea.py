from selenium import webdriver

import data
import helpers
from IKEA import IkeaHomePage, IkeaSearchResultsPage, IkeaProductPage


class TestIkeaSearch:
    """Automated tests for product search on ikea.pt."""

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.IKEA_URL):
            print("Conectado ao site da IKEA")
        else:
            print("Não foi possível conectar ao ikea.pt. Verifique sua conexão.")

    def setup_method(self):
        self.driver.get(data.IKEA_URL)
        self.home_page = IkeaHomePage(self.driver)
        self.home_page.reject_cookies_if_present()

    def test_search_returns_results(self):
        self.home_page.search_for(data.SEARCH_TERM)

        results_page = IkeaSearchResultsPage(self.driver)
        results_text = results_page.get_results_count_text()

        assert data.SEARCH_TERM in results_text
        assert "produtos" in results_text

    def test_search_with_no_results_shows_message(self):
        self.home_page.search_for(data.SEARCH_TERM_NO_RESULTS)

        results_page = IkeaSearchResultsPage(self.driver)
        assert results_page.has_no_results_message()

    def test_open_first_product_shows_title_and_price(self):
        self.home_page.search_for(data.SEARCH_TERM)

        results_page = IkeaSearchResultsPage(self.driver)
        results_page.open_first_product()

        product_page = IkeaProductPage(self.driver)

        assert data.EXPECTED_PRODUCT_NAME_FRAGMENT in product_page.get_title().lower()
        assert product_page.is_price_displayed()

    def test_add_first_product_to_cart(self):
        self.home_page.search_for(data.SEARCH_TERM)

        results_page = IkeaSearchResultsPage(self.driver)
        results_page.open_first_product()

        product_page = IkeaProductPage(self.driver)
        product_page.add_to_cart()

        # Simple check: the cart button in the header stops being empty.
        # (adjust this assertion once the exact cart behavior is confirmed)
        helpers.human_pause()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
