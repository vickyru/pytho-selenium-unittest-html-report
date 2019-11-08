from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import HtmlTestRunner
from test.page.calculator_page import CalculatorPage

class Calculator(unittest.TestCase):
    
    def setUp(self):
        try:
            # self.driver = webdriver.Firefox(executable_path=r'E:\web-drivers\geckodriver.exe')
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.driver.get('https://juliemr.github.io/protractor-demo/')
            self.driver.implicitly_wait(10)
        except Exception as exception:
            print("Exception Occured" + exception.with_traceback)
        
    def test_division(self):
        try:
            page = CalculatorPage(self.driver)
            page.enter_first_input(10)
            page.select_operator(1)
            page.enter_second_input(5)
            page.click_submit()
            result = page.get_output_text()
            self.assertEqual('2', result)
        except Exception as exception:
            print("Exception Occured" + exception.with_traceback)

    def test_addition(self):
        try:
            page = CalculatorPage(self.driver)
            page.enter_first_input(10)
            page.select_operator(0)
            page.enter_second_input(5)
            page.click_submit()
            result = page.get_output_text()
            self.assertEqual('15', result)
        except Exception as exception:
            print("Exception Occured" + exception.with_traceback)



    def test_percentage(self):
        try:
            page = CalculatorPage(self.driver)
            page.enter_first_input(50)
            page.select_operator(2)
            page.enter_second_input(100)
            page.click_submit()
            result = page.get_output_text()
            self.assertEqual('50', result)
        except Exception as exception:
            print("Exception Occured" + exception.with_traceback)

    def test_error(self):
        """ This test should be marked as error one. """
        raise ValueError

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass

    def tearDown(self):
            if self.driver is not  None :
                self.driver.close()
                self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='html-report', report_title='Dashboard Report', report_name='Calculator Test'),verbosity=1)
        