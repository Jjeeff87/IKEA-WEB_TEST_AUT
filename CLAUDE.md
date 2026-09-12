# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Selenium/pytest automated tests for the product search flow on ikea.pt (Portuguese IKEA site).

## Commands

```bash
pip install -r requirements.txt   # selenium, requests, pytest
pytest TestersiteIkea.py -v       # run all tests
pytest TestersiteIkea.py::TestIkeaSearch::test_search_returns_results -v  # run a single test
```

Requires a [ChromeDriver](https://chromedriver.chromium.org/) matching the local Chrome version, available on PATH. Tests drive a real Chrome browser against the live https://www.ikea.com/pt/pt/ site (no mocking), so they are network-dependent and can break if IKEA changes their markup or catalog.

## Architecture

Page Object Model, spread across four files:

- `data.py`: site URL and search terms (valid term, no-results term, expected product name fragment) used across tests.
- `helpers.py`: `is_url_reachable` (pre-flight site check), `human_type`/`human_pause` (see below).
- `IKEA.py`: Page Objects `IkeaHomePage` (search box, cookie banner), `IkeaSearchResultsPage` (results count, no-results message, first product link), `IkeaProductPage` (title, price, add-to-cart). Each page object takes the `driver` in `__init__` and wraps lookups in a `WebDriverWait`.
- `TestersiteIkea.py`: pytest test class `TestIkeaSearch`. One shared `driver` for the whole class (`setup_class`/`teardown_class`); each test navigates fresh from the home page (`setup_method`) and flows through the page objects (home to search results to product) rather than calling Selenium directly.

### Humanized typing

Instead of filling the search field instantly, `helpers.human_type` types character-by-character with small random delays, and `helpers.human_pause` adds short randomized pauses between actions. This exists to make the automation's interaction pace look more like a real person's rather than an obviously scripted fill-and-submit.

### Test cases covered

- Searching a valid term ("cadeira") returns results.
- Searching a nonexistent term shows the "Sem resultados para..." message.
- Opening the first product from results shows title and price.
- Adding the first product to the cart (assertion currently minimal/TODO, see comment in `test_add_first_product_to_cart`).

Locators (in `IKEA.py`) are XPath/CSS selectors tied to current ikea.pt markup and Portuguese-language text (e.g. "Rejeitar todos os cookies", "Adicionar ao cesto"). Expect to update them if the site's DOM or copy changes.
