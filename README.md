# SeleniumBasePythonAutoTest

## Before run:
* Install Python
* Initiate .venv
* Install pip:
  ```bash
  python -m pip install --upgrade pip && pip --version
  ```
* Install SeleniumBase:
  ```bash
  python -m pip install seleniumbase
  ```
* Install Allure Report:
  ```bash
  pip install allure-pytest
  ```

## Command line to run:
  ```bash
  python -m pytest --browser=$(browser) --alluredir=allure_results --ad-block --demo --demo-sleep=0 --highlights=3
  ```

## Generate Allure Report after run:
  ```bash
  allure serve allure-results
  ```
