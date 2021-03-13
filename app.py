# import libraries
from selenium import webdriver

def parseAddress(address):
    length = len(address)
    userStreetAddress = ''
    userCity = ''
    userState = ''
    userZipCode = ''
    for i, character in enumerate(address):
        if character == ',':
            userStreetAddress = (address[0:i])
            print(userStreetAddress)




print("Welcome to Find Your Reps!")
userAddress = input("Please input your address. For example: 555 Example Drive, Big Town, GA, 12345")
parseAddress(userAddress)









#web = webdriver.Firefox()
#web.get('https://www.house.gov/representatives/find-your-representative')
#zipCode = "30101"
#findZip = web.find_element_by_xpath('//*[@id="Find_Rep_by_Zipcode"]')
#findZip.send_keys(zipCode)
#submitButton = web.find_element_by_xpath('//*[@id="submit"]')
#submitButton.click()