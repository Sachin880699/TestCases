# 🧪 Pytest Selenium Automation Framework

This repository contains an automated testing framework using **Pytest** and **Selenium WebDriver**, structured with the Page Object Model (POM) design pattern.

---

## 🚀 Features

- Pytest-based test runner
- Page Object Model structure
- Parametrized tests
- Logging and HTML reporting with `pytest-html`
- Configurable browser setup
- Hooks for fixtures, setup, and teardown
- Example test for demo site: [demoqa.com](https://demoqa.com/checkbox)

---

## 👢 Project Structure

```
.
├── tests/
│   └── test_check_box.py        # Test cases
├── pages/
│   └── check_box_page.py        # Page object classes
├── conftest.py                  # Fixtures and hooks
├── requirements.txt             # Dependencies
├── README.md                    # This file
```

---

## 🔧 Installation

1. Clone the repo:

```bash
git clone https://github.com/your-username/pytest-selenium-demo.git
cd pytest-selenium-demo
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ✅ Running Tests

### Basic test run:

```bash
pytest
```

### With HTML report:

```bash
pytest --html=report.html --self-contained-html --capture=tee-sys
```

---

## 🍿 Pytest Marks Overview

| Mark                             | Description                      |
| -------------------------------- | -------------------------------- |
| `@pytest.mark.skip`              | Skip the test unconditionally    |
| `@pytest.mark.skipif(condition)` | Skip if condition is true        |
| `@pytest.mark.xfail`             | Test is expected to fail         |
| `@pytest.mark.parametrize(...)`  | Run a test with multiple inputs  |
| `@pytest.mark.usefixtures(...)`  | Apply fixture to a test or class |

Example:

```python
@pytest.mark.parametrize("search_term", ["Python", "Selenium"])
def test_google_search(search_term):
    ...
```

---

## 📊 Logging in Reports

Enable logging to be shown in `report.html`:

```python
# Inside test or conftest.py
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Test started")
```

Run with:

```bash
pytest --html=report.html --self-contained-html --capture=tee-sys
```

---

## 📦 Dependencies

Add to `requirements.txt`:

```
pytest
selenium
pytest-html
webdriver-manager
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🧹 Sample Test

```python
def test_check_box(browser):
    page = CheckBoxPage(browser)
    page.load()
    page.submit()
    output = page.get_output()
    assert "You have selected" in output
```

---

## 📄 License

MIT License

---

## 🤝 Contributing

Pull requests welcome! Please open issues for suggestions or bugs.

