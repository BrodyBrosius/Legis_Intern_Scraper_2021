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

    def parseAddress(self,address):
        length = len(address)
        addressArray = []
        k = 0
        for i, character in enumerate(address):
            k = k+1
            if character == ',':
                newAddressComponent = (address[0:k-1])
                addressArray.append(newAddressComponent)
                address = (address[k:length])
                length = len(address)
                k=0
            if(len(addressArray) == 3):
                addressArray.append(address)
                break
        self.removeSpacesFromAddressArray(addressArray)
        return addressArray

    def removeSpacesFromAddressArray(self,addressArray): #Removes spaces after commas between segments of the address
        for k, element in enumerate(addressArray):
            index = 0
            for index, item in enumerate(element):
                if(index == 0 and item == " "):
                    replacementString = ''
                    for i in range(1,len(element)):
                        replacementString = replacementString + element[i]
                    addressArray.remove(element)
                    addressArray.insert(k,replacementString)









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
        userAddress = input("Please input your address. For example: 555 Example Drive, Big Town, Georgia, 12345")
        addressArray = []
        addressArray = MainApp.parseAddress(self, userAddress)
        for i in addressArray:
            print(i)
        #MainApp.findFedRep(self)








newApp = MainApp()


