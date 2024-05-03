from CapsolverRecaptchaV3Bypasser import CapsolverRecaptchaV3Bypasser
from selenium import webdriver 
from selenium.webdriver.common.by import By  
import time

CAPSOLVER_API_KEY = "YOUR_CAPSOLVER_API_KEY"
PAGE_URL = "https://2captcha.com/demo/recaptcha-v3"
PAGE_KEY = "6LfB5_IbAAAAAMCtsjEHEHKqcB9iQocwwxTiihJu"

page = webdriver.Chrome()
page.get( PAGE_URL )
recaptchaBypasser = CapsolverRecaptchaV3Bypasser(page, PAGE_URL, PAGE_KEY, CAPSOLVER_API_KEY)

print("Solving reCaptcha v3...")
t0 = time.time()
recaptchaBypasser.solve_recaptcha()
print( f"Time elapsed: {time.time() - t0:.2f} seconds" )


buttons = page.find_elements(By.TAG_NAME,"button")
for button in buttons:
    if button.text == "Check":
        button.click()
        break

input("Press Enter to close the browser")

page.quit()

 