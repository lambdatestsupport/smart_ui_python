import unittest
import sys
import time
from selenium import webdriver
# import os

username = "sandhyas" # Replace the username
access_key = "6honM8azteHGSod0hN9273gFT36Tl5dKJfVdxzySqDhUNkRrcs"  # Replace the access key


class FirstSampleTest(unittest.TestCase):
    # Generate capabilities from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):
        desired_caps = {
            "build": 'PyunitTest sample test',  # Change your build name here
            "name": 'Py-unittest',  # Change your test name here
            "browserName": 'Chrome',
            "version": '112.0',
            "platform": 'Windows 11',
            "resolution": '1024x768', # change the resolution
            "network": 'true',  # Enable or disable network logs
            "smartUI.project": "kuch_bhi"
            # "smartUI.build": "Testing A"

            # Build name for smartUI(optional)
            #"smartUI.build" : "buildName",
        }
        self.driver = webdriver.Remote(
            command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            desired_capabilities={"LT:Options": desired_caps})

    # tearDown runs after each test case

    def tearDown(self):
        driver = self.driver

        #url
        driver.get("https://www.airvistara.com/in/en/vistara-exclusives/vistara-direct?gclid=Cj0KCQjwyLGjBhDKARIsAFRNgW_LjZ9aRWoNZWvgxsIkAf_3PqLAfLMiA63JBKtuCcZBEkHjatK1VusaAulZEALw_wcB&utm_source=google&utm_medium=cpc&utm_campaign=PMX_Brand_Dom_Search_Nov_22&ef_id=Cj0KCQjwyLGjBhDKARIsAFRNgW_LjZ9aRWoNZWvgxsIkAf_3PqLAfLMiA63JBKtuCcZBEkHjatK1VusaAulZEALw_wcB:G:s&s_kwcid=AL!596!3!636601358040!p!!g!!vistara&s_kwcid=AL!596!3!636601358040!p!!g!!vistara&gad=1")
        time.sleep(4)
        print("Taking screenshot")
    
        driver.execute_script("smartui.takeScreenshot,{\"screenshotName\":\"san-screenshot-1\"}")
        print("screenshot taken successfully")

        driver.quit()

    # """ You can write the test cases here """
    def test_unit_user_should_able_to_add_item(self):
        # try:
        driver = self.driver

        # Url
        driver.get("https://www.airvistara.com/in/en/vistara-exclusives/vistara-direct?gclid=Cj0KCQjwyLGjBhDKARIsAFRNgW_LjZ9aRWoNZWvgxsIkAf_3PqLAfLMiA63JBKtuCcZBEkHjatK1VusaAulZEALw_wcB&utm_source=google&utm_medium=cpc&utm_campaign=PMX_Brand_Dom_Search_Nov_22&ef_id=Cj0KCQjwyLGjBhDKARIsAFRNgW_LjZ9aRWoNZWvgxsIkAf_3PqLAfLMiA63JBKtuCcZBEkHjatK1VusaAulZEALw_wcB:G:s&s_kwcid=AL!596!3!636601358040!p!!g!!vistara&s_kwcid=AL!596!3!636601358040!p!!g!!vistara&gad=1")
        print("Taking screenshot")
        driver.execute_script("smartui.takeScreenshot,{\"screenshotName\":\"sample-screenshot-2\"}")
        print("screenshot taken successfully")

        driver.quit()
if __name__ == "__main__":
    unittest.main()
