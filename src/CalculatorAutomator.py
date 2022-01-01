from selenium import webdriver

import time

desired_caps = {
    "udid": "3b202ed30c20",
    "platformName": "Android",
    "platformVersion": "10",
    "appPackage": "com.continuum.emi.calculator",
    "appActivity": "com.finance.emicalci.activity.Splash_scren",
    "automationName": 'Uiautomator2',
    "noReset": "True"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

time.sleep(5)

driver.find_element_by_xpath("//*[@text='EMI Calculator' and ./parent::*[@id='btnStart']]").click()
time.sleep(4)

mEMI = 4568
tInterest = 9643
tpFee = 2000
tPayment = 109643

driver.find_element_by_xpath("//*[@id='rbLoanAmount']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='etLoanAmount']").send_keys("100000")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='etInterest']").send_keys("9.0")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='etYears']").send_keys("2")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='etMonths']").send_keys("0")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='etFee']").send_keys("2")
time.sleep(2)
driver.find_element_by_xpath("//*[@text='Calculate']").click()

result_mEMI = driver.find_element_by_xpath("//*[@id='monthly_emi_result']").text
if (result_mEMI == mEMI):
    print("Result Monthly EMI is Ok")
else:
    print("Monthly EMI is not Ok")

result_tInterest = driver.find_element_by_xpath("//*[@id='total_interest_result']").text
if (result_tInterest == tInterest):
    print("Result Total interest is Ok")
else:
    print("Total interest is not Ok")

result_tpFee = driver.find_element_by_xpath("//*[@id='processing_fee_result']").text
if (result_tpFee == tpFee):
    print("Result Processing fee is Ok")
else:
    print("Result Processing is not Ok")

result_tPayment = driver.find_element_by_xpath("//*[@id='total_payment_result']").text
if (result_tPayment == tPayment):
    print("Total payment EMI is Ok")
else:
    print("Total payment is not Ok")

time.sleep(10)

driver.close()
