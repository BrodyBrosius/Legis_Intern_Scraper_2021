# import libraries
from selenium import webdriver


web = webdriver.Firefox()
web.get('https://www.house.gov/representatives/find-your-representative')
zipCode = "30101"
findZip = web.find_element_by_xpath('//*[@id="Find_Rep_by_Zipcode"]')
findZip.send_keys(zipCode)
submitButton = web.find_element_by_xpath('//*[@id="submit"]')
submitButton.click()