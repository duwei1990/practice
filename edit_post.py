import unittest
from selenium import webdriver
from time import sleep
import login
 
class WordPressTestCase(unittest.TestCase):
   dr = None
   post_edit_url='http://localhost/wordpress/wp-admin/post.php?post=4&action=edit'
 
def setUp(self):
   self.dr=webdriver.Firefox()
 
def test_edit_post(self):
   self.login()
   self.edit_post(self)
 
def edit_post(self):
   self.dr.get('post_edit_url')
   content='my name is duwei'
   js="document.getElementById('content_ifr').contentWindow.document.body.innerHTML='"+content+"'"
   print js
   self.dr.execute_script(js)
   self.dr.find_element_by_name('publish').click()
   return content
 
def tearDown(self):
   self.dr.quit()
 
if __name__=='__main__':
   unittest.main()
