from selenium import webdriver
 
from time import sleep
 
def login(self):
dr =self.driver
login_url='http://localhost/wordpress/wp-login.php'
dr.get(login_url)
dr.find_element_by_name('log').send_keys('admin')
dr.find_element_by_name('pwd').send_keys('admin')
dr.find_element_by_name('wp_submit').click()
sleep(3)