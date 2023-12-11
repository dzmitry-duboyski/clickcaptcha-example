from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from PIL import Image
import requests
from twocaptcha import TwoCaptcha
solver = TwoCaptcha('YOUR_API_KEY')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
o = Options()
o.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=o)

#  Open target page
driver.get('https://2captcha.com/demo/clickcaptcha')

# save coordinates capthca
img_url = driver.find_element(By.CSS_SELECTOR, "img[alt='clickcaptcha example']").get_attribute('src')
img = Image.open(requests.get(img_url, stream = True).raw)
img.save('captcha.png')

# send coordinates captcha to the 2captcha service
result = solver.coordinates('./captcha.png')
# save coordinates in array
coordinates = result['code'].replace('coordinates:', "").replace('x=', "").replace('y=', "").split(';')


# creating variables for clicks on coordinates
coordinates1 = {'x1': 0,'y1': 0}
coordinates2 = {'x2': 0, 'y2': 0}
coordinates3 = {'x3': 0, 'y3': 0}

coordinates1['x1'] = coordinates[0].split(',')[0]
coordinates1['y1'] = coordinates[0].split(',')[1]
coordinates2['x2'] = coordinates[1].split(',')[0]
coordinates2['y2'] = coordinates[1].split(',')[1]
coordinates3['x3'] = coordinates[2].split(',')[0]
coordinates3['y3'] = coordinates[2].split(',')[1]

print("coordinates1=", coordinates1)
print("coordinates2=", coordinates2)
print("coordinates3=", coordinates3)

# Get an element with a captcha on a page
captcha_el = driver.find_element(By.CSS_SELECTOR, "img[alt='clickcaptcha example']")
# Getting the coordinates of a captcha element on a page
location_captcha = captcha_el.location
print("Captcha initial coordinates=", location_captcha)

# Move the cursor to the initial coordinates of the captcha, then move the cursor along the resulting coordinates, then click
ActionChains(driver).move_by_offset(captcha_el.location['x'], captcha_el.location['y']).move_by_offset(coordinates1['x1'], coordinates1['y1']).click().perform()
# Reset cursor coordinates
ActionChains(driver).reset_actions()
# Move the cursor to the initial coordinates of the captcha, then move the cursor along the resulting coordinates, then click
ActionChains(driver).move_by_offset(captcha_el.location['x'], captcha_el.location['y']).move_by_offset(coordinates2['x2'], coordinates2['y2']).click().perform()
# Reset cursor coordinates
ActionChains(driver).reset_actions()
# Move the cursor to the initial coordinates of the captcha, then move the cursor along the resulting coordinates, then click
ActionChains(driver).move_by_offset(captcha_el.location['x'], captcha_el.location['y']).move_by_offset(coordinates3['x3'], coordinates3['y3']).click().perform()


# Сlick on the 'check' button
button_el = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()