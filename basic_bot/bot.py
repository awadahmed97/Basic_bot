from config import keys
from selenium import webdriver



def order(k):

	driver = webdriver.Chrome('./chromedriver')
	#enters the site url (key in config file must be filled)
	driver.get(k['site_url'])
	#For click methods inspect element in chrome
	#and copy xpath of the tags you want to click
	#(Right click on link or button, then inspect element to see html code 
	#and go to the tag you want to copy and go to copy xpath)

	#EXAMPLES
	#driver.find_element_by_xpath('//*[@id="submit"]').click()
	#driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[1]/a"]').click()
	#driver.find_element_by_xpath('').click()
	#driver.find_element_by_xpath('').click()
	
	#send keys method will need two inputs
	#the first is the the xpath the same for the click method
	#the second is the config files keys that you want to use
	#remember ('') for xpath and ("") for keys in your config file
	#remember config file must be filled out for keys to be entered

	#EXAMPLES
	#driver.find_element_by_xpath('//*[@id="emailusername"]').send_keys(k["username"])
	#driver.find_element_by_xpath('//*[@id="emailpassword"]').send_keys(k["pass"])
	#driver.find_element_by_xpath('').send_keys(k[""])
	#driver.find_element_by_xpath('').send_keys(k[""])
	
	#when done filling them out put them in correct order depending on what
	#you want to click first or what keys to enter and when
	
	#EXAMPLE
	driver.find_element_by_xpath('').send_keys(k[""])
	driver.find_element_by_xpath('').send_keys(k[""])
	driver.find_element_by_xpath('').click()
	driver.find_element_by_xpath('').click()
	driver.find_element_by_xpath('').send_keys(k[""])

	#increase time if you need more time 
	time.sleep(500)

if __name__ == '__main__':

	order(keys)
