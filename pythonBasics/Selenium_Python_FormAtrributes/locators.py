
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name(By.NAME, "name").send_keys("Bharti")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Bharti")
driver.find_element(By.NAME, "email").send_keys("Sagar@bharti.com")

driver.find_element(By.ID,"exampleCheck1").click()

#select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(0)

driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "success" in message