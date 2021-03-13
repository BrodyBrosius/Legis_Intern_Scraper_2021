# import libraries
from selenium import webdriver

def parseAddress(address):
    print(address)
    length = len(address)
    userStreetAddress = ''
    userCity = ''
    userState = ''
    userZipCode = ''
    for i, character in enumerate(address):
        if character == ',':
            userStreetAddress = (address[0:i])
            address = (address[i+1:length])
            print(userStreetAddress)
            break
    for k, character in enumerate(address):
        if character == ',':
            userCity = (address[0:k])
            address = (address[k+1:length])
            print(userCity)
            break
    for x, character in enumerate(address):
        if character == ',':
            userState = (address[0:x])
            address = (address[x+1:length])
            print(userState)
            break
    userZipCode = address
    print(userZipCode)





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