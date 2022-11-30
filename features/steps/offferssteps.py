import pytest
import time
from behave import *
from selenium import webdriver
@given('launch the browser')
def step_impl(context):
    path = r"C:\Users\G P Varsha\Downloads\chromedriver_win32\chromedriver.exe"
    context.driver_obj = webdriver.Chrome(executable_path=path)



@when('open BookMyshow homepage')
def step_impl(context):
    context.driver_obj.get('https://in.bookmyshow.com/')
    time.sleep(5)



@when('choose city')
def step_impl(context):
    context.driver_obj.find_element("xpath", '(//span[text()="Bengaluru"])[1]').click()  # search for city
    time.sleep(5)


@then('Click on offers button')
def step_impl(context):
    context.driver_obj.find_element("xpath",'//a[@href="/offers"]').click()
    time.sleep(5)


@then('enter  "{input}" in search bar')
def step_impl(context,input):
    context.driver_obj.find_element("xpath", '//input[@type="text"]').send_keys(input)
    time.sleep(5)

@then('apply credit card filter')
def step_impl(context):
    context.driver_obj.find_element("xpath", '//p[text()="Credit Card"]').click()
    time.sleep(5)


@then('apply debit card filter')
def step_impl(context):
    context.driver_obj.find_element("xpath", '//p[text()="Debit Card"]').click()
    time.sleep(5)



@then('apply wallet filter')
def step_impl(context):
    context.driver_obj.find_element("xpath", '//p[text()="Wallet"]').click()
    time.sleep(5)