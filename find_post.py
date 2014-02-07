#coding=gbk
import unittest
from selenium import webdriver
from time import sleep
 
class WordPressTestCase(unittest.TestCase):
dr = None
post_list_url='http://localhost/wordpress/wp-admin/edit.php'
 
def setUp(self):
self.dr=webdriver.Firefox()
 
def test_find_post(self):
self.login(self)
self.find_post(self)
def find_post(self):
self.dr.get(post_list_url)
m=self.dr.find_element_by_id('cat')
m.find_element_by_xpath('//option[@value= "未分类"]')
 
def tearDown(self):
self.dr.quit()
 
if __name__=='__main__':
unittest.main()