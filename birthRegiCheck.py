from selenium import webdriver


def to_write(xpath, txt):
    return browser.find_element_by_xpath(xpath).send_keys(txt)


def date_of_birth(dob, mob, yob):
    return f'{yob}-{mob}-{dob}'


num = int(input('Enter Birth Registration Number: '))
dob = int(input('Date: '))
mob = int(input('Month: '))
yob = int(input('Year: '))

date = date_of_birth(dob, mob, yob)

path = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(path)
browser.maximize_window()
url = 'https://everify.bdris.gov.bd/'
browser.get(url)
browser.implicitly_wait(2)

to_write('//*[@id="ubrn"]', num)
to_write('//*[@id="BirthDate"]', date)

print('End - Close the window manually')
