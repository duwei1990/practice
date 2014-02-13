from selenium import webdriver
import unittest
import time

class TextField(unittest.TestCase):
    dr=None
    url='file:///C:/Users/Administrator/Desktop/homework.html'
    def setUp(self):
        self.dr=webdriver.Firefox()
        self.url='file:///C:/Users/Administrator/Desktop/homework.html'

    def test_tf(self):
        dr=self.dr
        dr.get(self.url)
        self.set(self)
        self.clear(self)
        self.click(self)
        #self.focus(self)
        ww=dr.find_element_by_id('tf')
        self.high_light(self,dr,ww)
    def set(self):
        self.dr.find_element_by_id('tf').send_keys('duwei')
        time.sleep(2)
        
    def clear(self):
        self.dr.find_element_by_id('tf').clear()

    def click(self):
        self.dr.find_element_by_id('tf').click()
    '''
    def focus(self):
        self.dr.

    '''
    def high_light(self,dr,ele):
        self.dr.execute_script("arguments[0].style.border='2px solid red'",self.ele)

    def tearDown(self):
        self.dr.quit()

if __name__=='__main__':
    unittest.main()
