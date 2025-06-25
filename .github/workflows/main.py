from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME = "your_dummy_username"
PASSWORD = "your_dummy_password"

# Setup
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)

# Login
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)
time.sleep(5)

# Search for account
search_box = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
search_box.send_keys("cbitosc")
time.sleep(3)
search_box.send_keys(Keys.RETURN)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

# Follow (only if not already followed)
try:
    follow_button = driver.find_element(By.XPATH, "//button[text()='Follow']")
    follow_button.click()
    time.sleep(2)
except:
    print("Already following or button not found.")

# Extract data
bio = driver.find_element(By.XPATH, "//div[@class='-vDIg']/span").text
stats = driver.find_elements(By.XPATH, "//ul[@class='_ac2a']/li/span/span")

posts = stats[0].get_attribute("innerText")
followers = stats[1].get_attribute("title")
following = stats[2].get_attribute("innerText")

# Write to file
with open("output.txt", "w") as f:
    f.write("CBIT OSC Instagram Profile Data\n")
    f.write(f"Bio: {bio}\n")
    f.write(f"Posts: {posts}\n")
    f.write(f"Followers: {followers}\n")
    f.write(f"Following: {following}\n")

driver.quit()
