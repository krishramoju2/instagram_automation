from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Dummy credentials
USERNAME = "testuser.cbitosc.auto"
PASSWORD = "Cbit@123456"

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Start driver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

# Login to Instagram
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)
time.sleep(7)

# Search for the account
search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_box.send_keys("cbitosc")
time.sleep(3)
search_box.send_keys(Keys.RETURN)
time.sleep(1)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

# Click Follow button if not followed
try:
    follow_button = driver.find_element(By.XPATH, "//div[text()='Follow' or text()='Following']")
    if follow_button.text == "Follow":
        follow_button.click()
        print("Followed cbitosc.")
        time.sleep(2)
    else:
        print("Already following cbitosc.")
except:
    print("Follow button not found.")

# Extract bio and statistics
try:
    bio = driver.find_element(By.XPATH, "//div[@class='-vDIg']/span").text
except:
    bio = "Bio not found."

try:
    stats = driver.find_elements(By.XPATH, "//ul[contains(@class,'x78zum5')]/li")
    posts = stats[0].text.split('\n')[0]
    followers = stats[1].text.split('\n')[0]
    following = stats[2].text.split('\n')[0]
except:
    posts = followers = following = "N/A"

# Write data to file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Instagram Profile Data: @cbitosc\n")
    f.write(f"Bio: {bio}\n")
    f.write(f"Posts: {posts}\n")
    f.write(f"Followers: {followers}\n")
    f.write(f"Following: {following}\n")

print("Data saved to output.txt")
driver.quit()
