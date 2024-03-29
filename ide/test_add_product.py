# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from constants import global_constants as c

class TestAddProduct():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_add_product(self):
    self.driver.get(c.BASE_URL)
    self.driver.maximize_window()
    self.driver.find_element(By.XPATH, "//input[@id=\'user-name\']").click()
    self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    self.driver.find_element(By.XPATH, "//input[@id=\'password\']").click()
    self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    self.driver.find_element(By.ID, "login-button").click()
    self.driver.find_element(By.XPATH, "//button[@id=\'add-to-cart-sauce-labs-backpack\']").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'shopping_cart_container\']/a/span").click()
    assert self.driver.find_element(By.XPATH, "//a[@id=\'item_4_title_link\']/div").text == "Sauce Labs Backpack"
    self.driver.find_element(By.XPATH, "//button[@id=\'continue-shopping\']").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").text == "Remove"
    self.driver.find_element(By.XPATH, "//button[@id=\'remove-sauce-labs-backpack\']").click()
    self.driver.close()
  
