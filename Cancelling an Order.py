from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='D:\JobEasy- Automation\python-selenium-automation\chromedriver.exe')
driver.maximize_window()

driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.XPATH, "//input[@type='search' and @id='helpsearch']")
search.send_keys('Cancel order')
sleep(2)
search.send_keys(Keys.RETURN)

element= driver.find_element(By.XPATH, "//h1['Cancel Items or Orders']")
assert 'Cancel Items or Orders' == element.text, f'An error message'
print('Test passed')

driver.quit()