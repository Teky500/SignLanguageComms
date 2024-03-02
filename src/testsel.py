from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://wecapable.com/tools/text-to-sign-language-converter/")
driver.find_element(by=By.NAME, value= 'srcText').send_keys("test two test again")
driver.find_element(by=By.NAME,value="Text2Sign").click()

html_source = driver.page_source
print(html_source)