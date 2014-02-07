import unittest
from selenium import webdriver
from time import sleep
import login
class WordPressTestCase(unittest.TestCase):
dr = None
post_edit_url='http://localhost/wordpress/wp-admin/post.php?post=7&action=edit'
def setUp(self):
self.dr=webdriver.Firefox()
 
def test_delete_post(self):
self.login(self)
self.delete_post(self)
print self.dr.current_url
self.assertTrue('trashed' in self.dr.current_url)
def delete_post(self):
self.dr.get(post_edit_url)
self.dr.find_element_by_class_name('submitdelete deletion').click()
 
def tearDown(self):
self.dr.quit()
 
if __name__=='__main__':
unittest.main()