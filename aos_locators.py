from faker import Faker
fake = Faker(locale='en_CA')
#---------------------------------------------------------
app = 'Advantage online shopping'
aos_url = 'https://advantageonlineshopping.com/#/'
aos_home_page_title = 'AdvantageDEMO'
aos_login_page_url = 'https://advantageonlineshopping.com/#/'
aos_login_page_title = '${nbsp}Advantage Shopping :Log in to the site'
aos_create_new_user = 'https://advantageonlineshopping.com/#/register'
# admin_username = 'first_name'
# admin_password = 'last_name'
# aos_dashboard_url =
# aos_dashboard_page_title =
# aos_add_new_user_page_title =
# ------------------------Fake date section------------------------------
first_name = fake.first_name()
last_name = fake.last_name()
new_username = f'{first_name}{last_name}'.lower()
new_password = fake.password()
email = f'{new_username}@{fake.free_email_domain()}'
middle_name = fake.first_name()
full_name = f'{first_name} {last_name} {fake.pyint(1111,2999)}'
phone_number = fake.phone_number()[:5]
country = fake.current_country()[:5]
city = fake.city()[:5]
address = fake.address().replace("\n", " ")[:10]  # '123 langara'
state = 'BC'  # fake.state()[:5]
postal_code = 'L6Y555'  # fake.postal_code()[:5]