from behave import *
from selenium import webdriver
from time import sleep
@given ("open the cpc application in firefox")
def step1(content):
    content.fb=webdriver.FirefoxProfile("C:/Users/kartseka/AppData/Roaming/Mozilla/Firefox/Profiles/hkn00nlo.Default User")
    content.driver=webdriver.Firefox(content.fb)
    content.driver.get("https://10.78.239.156/cupm/common/index.jsp")
    content.driver.implicitly_wait(20)
@when ('give username "{username}"')
def step2(content):
    content.driver.find_element_by_xpath(".//*[@id='loginPage_username']").click()
    sleep(3)
    content.driver.find_element_by_xpath(".//*[@id='loginPage_username']").send_keys(username)
    content.driver.implicitly_wait(20)
@when('give password "{password}"')
def step3(content):
    content.driver.find_element_by_xpath(".//*[@id='loginPage_password']").send_keys(password)
    content.driver.implicitly_wait(20)
@then ("click login")
def step4(content):
    content.driver.find_element_by_xpath(".//*[@id='loginPage_LoginButton_label']").click()
@then("wait for 25 sec")
def step5(content):
    sleep(25)
@then("close broswer")
def step6(content):
    content.driver.close()