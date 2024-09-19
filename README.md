# Capsolver GoogleRecaptchaV3 Bypass

[![Capsolver](docs/capsolver.png)](https://www.capsolver.com/?utm_source=github&utm_medium=ads&utm_campaign=scraping&utm_term=Capsolver-GoogleRecaptchaV3Bypass)

**Solve Google Recaptcha V3 in just one line of code!**

A Selenium implementation to bypass Google Recaptcha V3 using Capsolver API.

## Demo

![Demo](docs/demo.gif)

The captcha is solved in less than 2 seconds.

## Installation

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To use this script, you need to have a Capsolver account. You can create an account [here](https://dashboard.capsolver.com/passport/register?inviteCode=nqZvQXp_lveg) and get your API key. Once you have your API key, replace `YOUR_API_KEY` in the script with your actual API key.

Example usage:

```python
from CapsolverRecaptchaV2Bypasser import CapsolverRecaptchaV2Bypasser
from selenium import webdriver

CAPSOLVER_API_KEY = "YOUR_CAPSOLVER_API_KEY"
PAGE_URL = "https://2captcha.com/demo/recaptcha-v3"
PAGE_KEY = "6LfB5_IbAAAAAMCtsjEHEHKqcB9iQocwwxTiihJu"

page = webdriver.Chrome()
page.get( PAGE_URL )
recaptchaBypasser = CapsolverRecaptchaV3Bypasser(page, PAGE_URL, PAGE_KEY, CAPSOLVER_API_KEY)

recaptchaBypasser.solve_recaptcha()
```
## Test

To test the script, edit the `test.py` file and replace `YOUR API KEY` with your actual API key. Then run the following command:

```bash
python test.py
```

## Capsolver

Capsolver is a platform that provides APIs to solve CAPTCHAs. You can use Capsolver to bypass CAPTCHAs in your web scraping projects. The platform supports solving Google Recaptcha V2, Recaptcha V3, hCaptcha, FunCaptcha, GeeTest, and more. You can create an account [here](https://dashboard.capsolver.com/passport/register?inviteCode=nqZvQXp_lveg) and get your API key.
