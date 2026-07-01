from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers import human_type, human_pause


class IkeaHomePage:
    """Page Object da página inicial do ikea.pt (barra de busca)."""

    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[type="search"]')
    COOKIE_REJECT_BUTTON = (By.XPATH, '//button[contains(., "Rejeitar todos os cookies")]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def reject_cookies_if_present(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.COOKIE_REJECT_BUTTON)).click()
            human_pause()
        except Exception:
            pass

    def search_for(self, term):
        """Digita o termo de forma humanizada (caractere por caractere, com pausas) e confirma com Enter."""
        search_box = self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        search_box.click()
        human_pause(0.2, 0.6)
        human_type(search_box, term)
        human_pause()
        search_box.send_keys(Keys.RETURN)


class IkeaSearchResultsPage:
    """Page Object da página de resultados de busca (/search/?q=...)."""

    RESULTS_COUNT_TEXT = (By.XPATH, '//*[contains(text(), "produtos para")]')
    NO_RESULTS_TEXT = (By.XPATH, '//*[contains(text(), "Sem resultados para")]')
    FIRST_PRODUCT_LINK = (By.XPATH, '(//a[contains(@href, "/p/")])[1]')
    FIRST_PRODUCT_ADD_TO_CART_BUTTON = (By.XPATH, '(//button[contains(., "Adicionar") and contains(., "cesto")])[1]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def _find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def get_results_count_text(self):
        return self._find(self.RESULTS_COUNT_TEXT).text

    def has_no_results_message(self):
        try:
            return self._find(self.NO_RESULTS_TEXT).is_displayed()
        except Exception:
            return False

    def open_first_product(self):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_PRODUCT_LINK)).click()
        human_pause()

    def get_first_product_name(self):
        return self._find(self.FIRST_PRODUCT_LINK).text


class IkeaProductPage:
    """Page Object da página de detalhe de um produto."""

    PRODUCT_TITLE = (By.TAG_NAME, 'h1')
    PRICE = (By.XPATH, '//*[contains(text(), "€")]')
    QUANTITY_INPUT = (By.XPATH, '//input[@aria-label="Valor de entrada de quantidade"]')
    ADD_TO_CART_BUTTON = (By.XPATH, '(//button[contains(., "Adicionar ao cesto")])[1]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def _find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def get_title(self):
        return self._find(self.PRODUCT_TITLE).text

    def is_price_displayed(self):
        try:
            return self._find(self.PRICE).is_displayed()
        except Exception:
            return False

    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)).click()
        human_pause()
