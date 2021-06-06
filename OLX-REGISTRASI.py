from os import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome('/Applications/chromedriver90')
driver.maximize_window()
driver.get('https://www.olx.co.id/')
Driverwait = WebDriverWait(driver, 40)

Email = "ervs.label@gmail.com"
password = "Indonesia21"

#User click button login
BtnLgn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Login/Daftar')]")))
BtnLgn.click()

#User click login with email
ClckWthEmail = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//button[@data-aut-id='emailLogin']")))
ClckWthEmail.click()

#user input email
InputEmail = Driverwait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#email_input_field")))
InputEmail.send_keys(Email)

#click Lanjut
ClckLnjt = Driverwait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit'] span")))
ClckLnjt.click()
time.sleep(20)

#input password
inputPass = Driverwait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#password")))
inputPass.send_keys(password)

#konfimasi password
CnfrmPassword = Driverwait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#password-confirm")))
CnfrmPassword.send_keys(password)
time.sleep(10)
#click btn Buat kata sandi
BtnKtaSandi = driver.find_element_by_xpath("//span[normalize-space()='Buat kata sandi']")
BtnKtaSandi.click()

#UploadFoto 
btnUnggah = Driverwait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Unggah']")))
btnUnggah.send_keys("/Users/rizkaviosudiro/Desktop/profile.jpeg")

#click Lanjutkan
btnLnjtkn = Driverwait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Lanjutkan']")))
btnLnjtkn.click()

#Masukkan NoTelf 
# InputNumPhone = Driverwait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#phone")))
# InputNumPhone.send_keys("082175284846")

#click Lanjutkan 
BtnLanjut = Driverwait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Lanjutkan']")))
BtnLanjut.click()

#click Lanjutkan
BtnLanjut2 = Driverwait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Lanjutkan']")))
BtnLanjut2.click()

driver.quit()

