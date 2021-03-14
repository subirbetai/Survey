import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from libs.ADB import ADB
from libs.PC import PC

adb = ADB()
pc = PC()

# # Aeroplane Mode On Off
# adb.aeroplane(1)
# time.sleep(2)
# adb.aeroplane(0)
#
# # Enable Hotspot
# adb.hotspot(1)
#
# # Connect PC Wifi
# pc.connect_wifi('Red', '00000000')
#
# time.sleep(5)

driver = webdriver.Chrome()

hit = driver.get('https://cdnflair.com/srv.html?id=5501117&pub=1425423')

time.sleep(20)

try:

    occupation = Select(driver.find_element_by_xpath('//*[@id="ddlOccupationHL"]'))
    occupation.select_by_index(1)

    name = driver.find_element_by_xpath('//*[@id="txtNameHL"]')
    name.send_keys("SUBIR")

    mobile = driver.find_element_by_xpath('//*[@id="txtMobileHL"]')
    mobile.send_keys('9832453566')

    email = driver.find_element_by_xpath('//*[@id="txtEmailHL"]')
    email.send_keys('abc@gmail.com')

    loan = Select(driver.find_element_by_xpath('//*[@id="ddlPurposeOfLoanHL"]'))
    loan.select_by_index(2)

    live = driver.find_element_by_xpath('//*[@id="ddlCityHL"]')
    live.send_keys('KOLKATA')

    location = driver.find_element_by_xpath('//*[@id="txtPropertyLocationHL"]')
    location.send_keys('Kolaghat')

    dob = driver.find_element_by_xpath('//*[@id="txtDOBHL"]')
    dob.send_keys('16/01/1995')

    select_date = driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[2]/a')
    select_date.click()

    company = driver.find_element_by_xpath('//*[@id="txtCompanyHL"]')
    company.send_keys('RE ONLINE SERVICE')

    salary = driver.find_element_by_xpath('//*[@id="txtGrossSalaryHL"]')
    salary.send_keys('30000')

    emi = driver.find_element_by_xpath('//*[@id="txtEMIHL"]')
    emi.send_keys('0')

    submit = driver.find_element_by_xpath('//*[@id="btnSubmitHL"]')
    submit.click()
except:
    print('Unable to Fill Data')

time.sleep(7)
print('Chrome Closed')
driver.quit()
