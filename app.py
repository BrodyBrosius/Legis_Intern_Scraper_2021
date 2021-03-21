# import libraries
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


class MainApp:
    def __init__(self):
        self.userStreetAddress = ''
        self.userCity = ''
        self.userState = ''
        self.userStatePostalCode = ''
        self.userZipCode = ''
        self.StatePostalCodeDict = dict(
            {'AL': 'Alabama',
             'AK': 'Alaska',
             'AZ': 'Arizona',
             'AR': 'Arkansas',
             'CA': 'California',
             'CO': 'Colorado',
             'CT': 'Conneticut',
             'DE': 'Delaware',
             'DC': 'District of Columbia',
             'FL': 'Florida',
             'GA': 'Georgia',
             'HI': 'Hawaii',
             'ID': 'Idaho',
             'IL': 'Illinois',
             'IN': 'Indiana',
             'IA': 'Iowa',
             'KS': 'Kansas',
             'KY': 'Kentucky',
             'LA': 'Louisiana',
             'ME': 'Maine',
             'MD': 'Maryland',
             'MA': 'Massachusetts',
             'MI': 'Michigan',
             'MN': 'Minnesota',
             'MS': 'Mississippi',
             'MO': 'Missouri',
             'MT': 'Montana',
             'NE': 'Nebraska',
             'NV': 'Nevada',
             'NH': 'New Hampshire',
             'NJ': 'New Jersey',
             'NM': 'New Mexico',
             'NY': 'New York',
             'NC': 'North Carolina',
             'ND': 'North Dakota',
             'OH': 'Ohia',
             'OK': 'Oklahoma',
             'OR': 'Oregon',
             'PA': 'Pennsylvania',
             'PR': 'Puerto Rico',
             'RI': 'Rhode Island',
             'SC': 'South Carolina',
             'SD': 'South Dakota',
             'TN': 'Tennessee',
             'TX': 'Texas',
             'UT': 'Utah',
             'VT': 'Vermont',
             'VA': 'Virgina',
             'VI': 'Virgin Islands',
             'WA': 'Washington',
             'WI': 'Wisconsin',
             'WY': 'Wyoming',
             })
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

    def defineAddressVariables(self, addressArray):
            self.userStreetAddress = addressArray[0]
            self.userCity = addressArray[1]
            if(len(addressArray[2]) == 2):
                self.userState = self.StatePostalCodeDict.get(addressArray[2])
            else:
                self.userState = addressArray[2]
            self.userZipCode = addressArray[3]

    def editDeliveredRepString(self,text):
        for index, item in enumerate(text):
            if (item == '('):
                text = (text[0:index-1])
                break
        return text


    def findFedRep(self):
        web = webdriver.Firefox()
        web.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
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
        stateDropDown.select_by_visible_text(self.userState)
        finalSubmitButton = web.find_element_by_xpath('/html/body/div[2]/div/div[2]/section/div/div[2]/div[1]/div[1]/div[1]/form/div[3]/input')
        finalSubmitButton.click()
        userFederalRep = web.find_element_by_class_name("ext")
        repDeliveredString = userFederalRep.get_attribute("text")
        print("Your Representative in the U.S. House of Representatives is: " + self.editDeliveredRepString(repDeliveredString))


    def appStart(self):
        print("Welcome to Find Your Reps!")
        userAddress = input("Please input your address. For example: 555 Example Drive, Big Town, Georgia, 12345")
        addressArray = []
        addressArray = MainApp.parseAddress(self, userAddress)
        self.defineAddressVariables(addressArray)
        MainApp.findFedRep(self)









newApp = MainApp()


