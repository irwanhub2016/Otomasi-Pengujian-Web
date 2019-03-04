from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re, datetime
import os
import random
import HtmlTestRunner
from dotenv import load_dotenv

load_dotenv()
from pathlib import Path  # python3 only

env_path = '.env'
load_dotenv(dotenv_path=env_path)


class TestProductCategoryEvening(unittest.TestCase):
	def setUp(self):
		
		options = webdriver.ChromeOptions()
		options.add_argument("--incognito")
		options.add_argument("--headless")
		options.add_argument("--no-sandbox")
		options.headless = True
		self.driver = webdriver.Chrome(chrome_options=options)
		
		# self.driver = webdriver.Chrome()
		self.verificationErrors = []
		self.accept_next_alert = True
	
	def test_product_category_evening(self):
		
		driver = self.driver
		x = datetime.datetime.now()
		y_minutes = x.strftime("%M")
		y_hours = x.strftime("%H")
		get_time_minutes = int(y_minutes) + 2
		get_time_hours = int(y_hours)
		get_url = os.getenv("URL")
		
		# delete session
		driver.delete_all_cookies()
		
		'''Akses halaman utama web'''
		print("-> Akses website Automation Practice")
		driver.get(get_url)
		
		try:
			
			'''Akses halaman utama web'''
			element = WebDriverWait(driver, 5).until(
				EC.presence_of_element_located((By.XPATH, "//img[@class='logo img-responsive']")))
			print("-> Berhasil akses halaman utama web")
			
			'''Pindah ke tab WOMEN'''
			element_tab_women = driver.find_element(By.XPATH, "//a[@title='Women']")
			action = webdriver.ActionChains(driver)
			action.move_to_element(element_tab_women)
			action.perform()
			print("-> Akses kategori Evening Dresses pada Tab WOMEN")
			
			time.sleep(1)
			
			validation_hover_element = driver.find_element(By.XPATH,
			                                               "/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[6]/ul[1]/li[1]/ul[1]")
			
			element_evening = driver.find_element(By.XPATH,
			                                      "/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[6]/ul[1]/li[1]/ul[1]/li[2]/ul[1]/li[2]/a[1]")
			element_evening.click()
			
			access_page_evening = WebDriverWait(driver, 5).until(
				EC.presence_of_element_located((By.XPATH, "//span[@class='category-name']")))
			
			validation_page_evening = driver.find_element(By.XPATH, "//span[@class='category-name']")

			'''Validasi Kategori Evening Dresses dapat diakses'''
			if validation_page_evening.text == 'Evening Dresses':
				print("-> Halaman Kategori Evening Dresses berhasil diakses")
				time.sleep(3)
			
			else:
				print("-> Halaman Kategori Evening Dresses tidak sesuai ekspetasi")
				time.sleep(3)
				raise Exception
			
			time.sleep(3)
		
		except Exception as e:
			print(e)
			raise
	
	def is_element_present(self, how, what):
		try:
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e:
			return False
		return True
	
	def is_alert_present(self):
		try:
			self.driver.switch_to_alert()
		except NoAlertPresentException as e:
			return False
		return True
	
	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally:
			self.accept_next_alert = True
	
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
	unittest.main()
	# unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./'), failfast=False, buffer=False,
	#               catchbreak=False)