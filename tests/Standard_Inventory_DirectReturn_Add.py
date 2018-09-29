from config.configs import Configs
from utils.login import Login
from utils.signout import SignOut
from utils.simulate import Simulate
from time import sleep

# Login to Login Page
Login().login(Configs.url, Configs.usr, Configs.pwd)

# Dashboard Opened
print("Dashboard Opened")


# Opening side menu Item Maintenance
Simulate().click_by_xpath("/html/body/div/aside/section/ul/li[5]/a")
# Opening side menu Item Maintenance's Menu Items
Simulate().click_by_xpath("//*[@id='directreturn']/a")
print("Opened Direct Return")
sleep(1)

# Checking if Add Button is disabled
if Simulate().get_attribute_by_id("add","disabled") == "disabled":
    print("Add Direct Receiving Opened")
else:
    Simulate().click_by_id("add")
    print("Add Direct Receiving Opened")
    sleep(1)
Configs.drv.find_element_by_xpath("//div[@id='DirectReturn_SUP_CODE_chzn']").click()
print("Supplier Dropdown Opened")
# Simulate().click_by_xpath("//div[@id='DirectReturn_SUP_CODE_chzn']")
# elem = Simulate().get_elements_by_xpath("//*[@id='DirectReturn_SUP_CODE_chzn']/div/ul/li")
# elem = Simulate().get_elements_by_xpath("//div[@id='DirectReturn_SUP_CODE_chzn']//div[@class='chzn-drop']//ul[@class='chzn-results']")
# print(elem[0].text)
# exit()
elem = Simulate().get_elements_by_xpath("//div[@id='DirectReturn_SUP_CODE_chzn']//div[@class='chzn-drop']//ul//li")
no_of_elements = len(elem)
for x in xrange(no_of_elements):
    print("["+str(x+1)+"] ("+elem_text[x]+")")
no_of_elements += 1
cond=0
elem_text = {}
while cond <= 0 or cond > no_of_elements:
    cond = input("Choose a Supplier: ")
    if cond <= 0:
        print("Error: Minimum is 1")
    if cond > no_of_elements:
        print("Error: Maximum is " + str(no_of_elements))
cond =- 1
Simulate().down_enter(cond)
print("Added Supplier: "+ elem_text[cond])
sleep(1)

Configs.drv.find_element_by_xpath("//div[@id='DirectReturn_LOC_CODE_chzn']").click()
#Simulate().click_by_xpath("//div[@id='DirectReturn_LOC_CODE_chzn']//div[@class='chzn-drop']//ul//li[@id='DirectReturn_LOC_CODE_chzn_o_0']")
elem = Simulate().get_elements_by_xpath("//div[@id='DirectReturn_LOC_CODE_chzn']//div[@class='chzn-drop']//ul//li")
no_of_elements = len(elem)
for x in xrange(no_of_elements):
    print("["+str(x)+"] ("+elem[x].text+")")
no_of_elements += 1
cond=0
while cond <= 0 or cond > no_of_elements:
    cond = input("Choose a Location: ")
    if cond <= 0:
        print("Error: Minimum is 1")
    if cond > no_of_elements:
        print("Error: Maximum is " + str(no_of_elements))
cond =- 1
Simulate().down_enter(cond)
print("Added Location: "+ elem[cond].text)
sleep(1)

# Simulate().click_by_xpath("//div[@id='DirectReturn_LOC_CODE_chzn']")
# Simulate().click_by_xpath("//div[@id='DirectReturn_LOC_CODE_chzn']//div[@class='chzn-drop']//ul[@class='chzn-results']//li[@id='DirectReturn_LOC_CODE_chzn_o_0']")
print("Added Location")

elem = Configs.drv.find_element_by_xpath("//table[@id='DataTables_Table_0']//tbody[@class='myDatatableClass']//tr[@class='odd']//td") #[0]
Configs.drv.execute_script("arguments[0].click();", elem)
Simulate().double_enter()

print("Opened Search Modal")
sleep(1)

while True:
    # Receiving Input of User
    search_code=raw_input("Enter Search Code: ")
    # Insert the Data
    Simulate().input_by_id("keyword", search_code)
    print("Entered Search Code " + search_code)
    sleep(1)

    # Display Results
    print("Displayed Item with Search Code: " + search_code)
    # Checking Results
    if Simulate().get_text_by_xpath("//*[@id='lookUp_search']/div[1]/table/tbody/tr/td") == "No results found or no SUPPLIER selected.":
        print("No results found or no SUPPLIER selected.")
    else:
        no_of_items=len(Simulate().get_elements_by_xpath("//*[@id='lookUp_search']/div[1]/table/tbody/tr[@class='can_be_selected']"))#"))
        print("Please refer to the number of items on the list given by the modal.")
        if no_of_items > 1:
            while True:
                down=input("Enter how many down arrows? [1-"+str(no_of_items)+"] ")
                if down <= no_of_items and down != 0:
                    # Selecting the Item and Displaying
                    Simulate().down_enter(down)    
                    break
                else:
                    print("Only "+str(no_of_items)+" are only available!")
        break

# Configs.drv.find_element_by_xpath("//div[@id='DirectReturn_BRN_CODE_chzn']").click()
# Configs.drv.find_element_by_xpath("//div[@id='DirectReturn_BRN_CODE_chzn']//div[@class='chzn-drop']//ul[@class='chzn-results']//li[@id='DirectReturn_BRN_CODE_chzn_o_1']").click()
# print("Added Branch")

Simulate().click_by_id("save")
print("Save")

sleep(1)
print("Ready for print")
Simulate().click_by_xpath("/html/body/div[3]/div/div/div[2]/button[1]")
Simulate().click_by_xpath("//*[@id='post']")
sleep(3)
Simulate().click_by_xpath("/html/body/div[3]/div/div/div[2]/button[1]")

# sleep(1)
# SignOut().signOut()
# Configs.drv.close()
# exit()
