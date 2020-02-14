from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
assert "Facebook" in driver.title
elem_mail = driver.find_element_by_id("email")
elem_mail.send_keys("youremail@yourdomain")
elem_pass = driver.find_element_by_id("pass")
elem_pass.send_keys("*** or your password")
guzik = driver.find_element_by_id("loginbutton")
guzik.click()
