from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://login.salesforce.com/")
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("Bharti")
driver.find_element(By.CSS_SELECTOR, ".password").send_keys("Sagar")
driver.find_element(By.CSS_SELECTOR, ".password").clear()
driver.find_element(By.LINK_TEXT, "Forgot Your Password?").click()
#//tagname[text()=’xxx’]
driver.find_element(By.XPATH, "//a[text()='Cancel']").click()
print(driver.find_element(By.XPATH, "//form[@name='login']/div[1]/label").text)
print(driver.find_element(By.CSS_SELECTOR, "form[name='login'] label:nth-child(3)").text)





