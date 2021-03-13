# import libraries
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class MainApp:
    def __init__(self):
        self.userStreetAddress = ''
        self.userCity = ''
        self.userState = ''
        self.userZipCode = ''
        self.appStart()

    def parseAddress(self, address):
        length = len(address)
        for i, character in enumerate(address):
            if character == ',':
                self.userStreetAddress = (address[0:i])
                address = (address[i + 1:length])
                break
        for k, character in enumerate(address):
            if character == ',':
                self.userCity = (address[0:k])
                address = (address[k + 1:length])
                break
        for x, character in enumerate(address):
            if character == ',':
                self.userState = (address[0:x])
                address = (address[x + 1:length])
                break
        self.userZipCode = address
        int(self.userZipCode)





    def findFedRep(self):
        web = webdriver.Firefox()
        web.get('https://www.house.gov/representatives/find-your-representative')
        findZip = web.find_element_by_xpath('//*[@id="Find_Rep_by_Zipcode"]')
        findZip.send_keys(self.userZipCode)
        submitButton = web.find_element_by_xpath('//*[@id="submit"]')
        submitButton.click()
        findStreetAddress = web.find_element_by_xpath('//*[@id="street"]')
        findStreetAddress.send_keys(self.userStreetAddress)
        findCity = web.find_element_by_xpath('//*[@id="city"]')
        findCity.send_keys(self.userCity)
        stateDropDown = Select(web.find_element_by_id("state"))
        stateDropDown.select_by_visible_text("Georgia")
        finalSubmitButton = web.find_element_by_xpath('/html/body/div[2]/div/div[2]/section/div/div[2]/div[1]/div[1]/div[1]/form/div[3]/input')
        finalSubmitButton.click()
        userFederalRep = web.find_element_by_class_name("ext")
        print(userFederalRep.get_attribute("text"))


    def appStart(self):
        print("Welcome to Find Your Reps!")
        userAddress = input("Please input your address. For example: 555 Example Drive, Big Town, GA, 12345")
        MainApp.parseAddress(self, userAddress)
        MainApp.findFedRep(self)








newApp = MainApp()


