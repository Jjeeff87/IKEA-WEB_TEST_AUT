# SiteIKEA: Test Automation (ikea.pt product search)

The first project in this series: automated Python/Selenium tests for the
**product search** flow on the [ikea.pt](https://www.ikea.pt) site. The Page
Object Model structure I use here ended up becoming the starting point for the
other automation projects on my list.

## Structure

| File | Role |
|---|---|
| `data.py` | Site URL and search terms used in the tests |
| `helpers.py` | Utilities: checking that the site is up, "humanized" typing/pauses |
| `IKEA.py` | Page Objects: `IkeaHomePage`, `IkeaSearchResultsPage`, `IkeaProductPage` |
| `TestersiteIkea.py` | Pytest tests |

## About "humanized" typing

Instead of filling the search field instantly, `helpers.human_type` types
character by character with small random pauses, and `helpers.human_pause`
inserts short pauses between actions, giving the automation a pace closer to
that of a real person interacting with the site.

## Test cases

- Searching for a valid term ("cadeira") returns results.
- Searching for a nonexistent term shows the "Sem resultados para..." message.
- Opening the first product in the list shows its title and price.
- Adding the first product to the cart.

## Installation

```bash
pip install -r requirements.txt
```

Requires [ChromeDriver](https://chromedriver.chromium.org/) matching your
Chrome version, available on PATH.

## Running the tests

```bash
pytest -v
```

The project's `pytest.ini` configures pytest to recognize `TestersiteIkea.py`
as a test file (its name does not follow the `test_*.py` pattern that pytest
looks for by default), so `pytest -v` on its own already finds and runs
everything.

## Code quality

```bash
pip install -r requirements-dev.txt
black --check .
flake8 .
```

CI (GitHub Actions, in `.github/workflows/tests.yml`) installs Chrome and
runs the full suite on every push/PR.

## Publishing to GitHub

```bash
git add .
git commit -m "Product search test automation - ikea.pt"
git remote add origin <URL_OF_YOUR_GITHUB_REPOSITORY>
git push -u origin master
```
</content>
</invoke>
