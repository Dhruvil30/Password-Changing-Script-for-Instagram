from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

UserName = input("Enter your username : ")
PassWord = input("Enter your password : ")
newPassWord = input("Enter your new password : ")

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver")
driver.get("https://www.instagram.com")

username = WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.NAME, 'username')))
username.send_keys(UserName)

password = driver.find_element_by_name('password')
password.send_keys(PassWord)

password.send_keys(Keys.RETURN)

notnowButton = WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[3]/button[2]')))
notnowButton.click()

userButton = WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')))
userButton.click()

userName = WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/h2')))
print(userName.text)

userInfo = WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul')))
print(userInfo.text)

editButton = WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/a/button')))
editButton.click()

changepassButton = WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/ul/li[2]/a')))
changepassButton.click()

oldpassEntry = WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.XPATH,'//*[@id="cppOldPassword"]')))
oldpassEntry.send_keys(PassWord)

passEntry = WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.XPATH,'//*[@id="cppNewPassword"]')))
passEntry.send_keys(newPassWord)

RepassEntry = WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.XPATH,'//*[@id="cppConfirmPassword"]')))
RepassEntry.send_keys(newPassWord)

confirmButton = WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/article/form/div[4]/div/div/button')))
confirmButton.click()

driver.back()
driver.back()

settingButton = WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button')))
settingButton.click()

logoutButton = WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/button[9]')))
logoutButton.click()

time.sleep(3)

driver.quit()