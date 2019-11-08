from selenium import webdriver
from selenium.webdriver.support.ui import Select
from test.locators.calculator_loc import Locators

class CalculatorPage():
    ''' Page Object class for calculator page '''

    def __init__(self, driver):
        self.driver = driver

    def enter_first_input(self, first_input):
        self.driver.find_element_by_xpath(Locators.first_input).send_keys(first_input)

    def select_operator(self, index):
        selectOperator = Select(self.driver.find_element_by_xpath(Locators.select_operator))
        selectOperator.select_by_index(index)

    def enter_second_input(self, second_input):
        self.driver.find_element_by_xpath(Locators.second_input).send_keys(second_input)

    def click_submit(self):
        self.driver.find_element_by_xpath(Locators.submit_button).click()
    
    def get_output_text(self):
        return self.driver.find_element_by_xpath(Locators.result_text).text