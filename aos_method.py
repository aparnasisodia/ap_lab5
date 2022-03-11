import sys
from selenium import webdriver # import selenium to the file
import aos_locators as locators
from selenium.webdriver.chrome.service import Service
import time
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # <-- add this import for drop down lists
from selenium.webdriver.common.keys import Keys
from faker import Faker

fake = Faker(locale='en_CA')

print('----------------------------******--------------------------------------------------')
print('---------------------------*****---------------------------------------------------------')


# ------------------------Fake date section------------------------------
first_name = fake.first_name()
last_name = fake.last_name()
middle_name = fake.first_name()
full_name = f'{first_name} {last_name} {{fake.pyint(11,2999)}}'
new_username = f'{first_name}{last_name}'.lower()
new_password = fake.password()
email = f'{new_username}@{fake.free_email_domain()}'
phone_number = fake.phone_number()[:5]
country = fake.current_country()[:5]
city = fake.city()[:5]
address = fake.address().replace("\n", " ")[:10]  # '123 langara'
state = 'BC'  # fake.state()[:5]
postal_code = 'L6Y555'  # fake.postal_code()[:5]
# ------------------------------------------------------------------------
list_list = ['new_username', 'email', 'new_password', 'first_name', 'last_name', 'phone_number', 'country',
             'city', 'address', 'state', 'postal_code', 'new_username', 'phone_number', 'country', 'city', 'address',
             'state', 'postal_code']

list_name = ['usernameRegisterPage', 'emailRegisterPage', 'passwordRegisterPage', 'confirm_passwordRegisterPage',
             'first_nameRegisterPage', 'last_nameRegisterPage', 'phone_numberRegisterPage', 'countryListboxRegisterPage'
    , 'cityRegisterPage', 'addressRegisterPage', 'state_/_province_/_regionRegisterPage', 'postal_codeRegisterPage']

# ---------------------------------------------------------------------------------
driver = webdriver.Chrome('/Users/owner/Desktop/pythonProject/venv/chromedriver 2')

def setUp():
    print(f'The testing was started at: {datetime.datetime.now()}')
    print('---------------------------------------------------')
    print(f'Chrome web browser  is opened')
    driver.implicitly_wait(30)
    driver.maximize_window()
    time.sleep(.3)
    # 3. Navigate to web page URL - 'https://advantageonlineshopping.com/#/' (Links to an external site.)
    driver.get(locators.aos_url)
    time.sleep(2)
    # 4. Check URL and home page title are as expected.
    print(driver.current_url)
    print(driver.title)
    if driver.current_url == locators.aos_url and driver.title == locators.aos_home_page_title:
        print(f' The URL is : {driver.current_url} and the title of the web-page is :{driver.title}')

def tearDown():
    if driver is not None:
        print('--------------------~*~--------------------')
        print(f'The test Completed at: {datetime.datetime.now()}')
        time.sleep(2)
        driver.close()
        driver.quit()


# Create New Account - using Faker library fake data
def create_new_user():
    driver.find_element(By.ID, 'menuUserLink').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT , 'CREATE NEW ACCOUNT').click()
    time.sleep(2)
    driver.find_element(By.NAME,'usernameRegisterPage').send_keys(locators.new_username)
    time.sleep(.3)
    driver.find_element(By.NAME,'emailRegisterPage').send_keys(locators.email)
    time.sleep(.3)
    driver.find_element(By.NAME,'passwordRegisterPage').send_keys(locators.new_password)
    time.sleep(.3)
    driver.find_element(By.NAME,'confirm_passwordRegisterPage').send_keys(locators.new_password)
    time.sleep(2)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    time.sleep(2)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    time.sleep(.25)
    # driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(phone_number)
    # time.sleep(.25)
    # Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(country)
    # time.sleep(.25)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    time.sleep(.25)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
    time.sleep(.25)
    x = driver.find_element(By.NAME, 'i_agree').is_selected()
    if x == False :
        driver.find_element(By.NAME, 'i_agree').click()
    else :
        print('Problem in registering')
        driver.close()
    time.sleep(3)
    driver.find_element(By.ID, 'register_btnundefined').click()
    time.sleep(2)
    print(f' the registered  username is  : "{locators.new_username}" and password is: "{locators.new_password}"')
    # logger('created')


# Logout
def log_out():
    driver.find_element(By.ID, 'menuUserLink').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    print('---------------*%*----------------')
    print(f'The {driver.current_url} was closed at: {datetime.datetime.now()}')
    # driver.close()
    # driver.quit()


# login
def log_in():
    if driver.current_url == locators.aos_url and driver.title == locators.aos_home_page_title:
        print(f' The URL is : {driver.current_url} and the title of the web-page is :{driver.title}')
    else:
        print(f' Something is wrong. Check the URL of the web page!')
    time.sleep(2)
    driver.find_element(By.ID, 'menuUser').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    driver.find_element(By.NAME,'password').send_keys(locators.new_password)
    time.sleep(.3)
    driver.find_element(By.ID,'sign_in_btnundefined').click()
    time.sleep(4)
    # CHECK-LOGIN
    x = driver.find_element(By.XPATH, f'//*[@id="menuUserLink"]/span[contains(.,"{locators.new_username}")]').is_displayed()
    print(x)
    if x == True:
        print(f' login was successful')
    else:
        print(f' THERE IS A PROBLEM- CAN YOU HELP ME PLEASE FIND IT??')


#logger
def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.new_username}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()

setUp()
create_new_user()
log_out()
log_in()
logger('created')
tearDown()

# setUp()
# create_new_user()
# log_out()
# log_in()
# logger('created')
# tearDown()