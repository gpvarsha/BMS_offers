from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
path=r"C:\Users\G P Varsha\Downloads\chromedriver_win32\chromedriver.exe"
driver_obj = webdriver.Chrome(executable_path=path)
driver_obj.get('https://in.bookmyshow.com/')
driver_obj.maximize_window()
time.sleep(2)
driver_obj.find_element("xpath",'(//span[text()="Bengaluru"])[1]').click() #search for city
driver_obj.find_element("xpath",'//a[@href="/offers"]').click()
time.sleep(3)
driver_obj.find_element("xpath",'//input[@type="text"]').send_keys('sbi')
time.sleep(2)

act = ActionChains(driver_obj)
act.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)


driver_obj.refresh()

driver_obj.find_element("xpath",'//p[text()="Credit Card"]').click()
time.sleep(2)
act = ActionChains(driver_obj)
act.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)
driver_obj.find_element("xpath",'//h4[text()="AURUM Credit Card Offer"]').click()
time.sleep(2)
driver_obj.find_element("xpath",'//a[@href="/offers"]').click()
time.sleep(2)
driver_obj.find_element("xpath",'//p[text()="Debit Card"]').click()
time.sleep(2)
act = ActionChains(driver_obj)
act.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)
driver_obj.find_element("xpath",'//h4[text()="VISA INFINITE PROGRAM"]').click()
time.sleep(2)
driver_obj.find_element("xpath",'//a[@href="/offers"]').click()
time.sleep(2)
driver_obj.find_element("xpath",'//p[text()="Wallet"]').click()
time.sleep(2)
act = ActionChains(driver_obj)
act.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)

driver_obj.find_element("xpath",'//h4[text()="Paytm CashBack Offer"]').click()
time.sleep(2)
driver_obj.find_element("xpath",'//a[@href="/offers"]').click()
time.sleep(2)
