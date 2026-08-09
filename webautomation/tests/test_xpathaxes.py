from playwright.sync_api import Page, expect

# 1. following-sibling:
# enter the salary for person Sachin Tendulkar
def test_entersalaryforpersonsachin(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/WebTableHTML.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//td[text()='Sachin Tendulkar']/following-sibling::td/following-sibling::td/following-sibling::td/following-sibling::td/input").fill("25000")
    page.wait_for_timeout(2000)

# 2. following:
# Enter the salary for person who is next to Sachin Tendulkar
def test_entersalarywhoisnexttosachintendulkar(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/WebTableHTML.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//td[text()='Sachin Tendulkar']/following::tr[1]/td[6]/input").fill("15000")
    page.wait_for_timeout(2000)

# 3. preceding-sibling
# Make status Active for Indian Freedom Fighter
def test_makestatusactiveforindianfreedomfighter(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/WebTableHTML.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//td[text()='Indian Freedom Fighter']/preceding-sibling::td[1]/preceding-sibling::td[1]/input").click()
    page.wait_for_timeout(2000)

# 4. preceding
# Make status as Active for Person who is previous to Rahul Dravid
def test_makestatusactiveforpersonwhoisprevioustorahuldravid(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/WebTableHTML.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//td[text()='Rahul Dravid']/preceding::tr[1]/td[1]/input").click()
    page.wait_for_timeout(2000)

# 5. ancestor
# Based on Salary edit text field identify the table
def test_fetchattributeoftable(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/WebTableHTML.html")
    page.wait_for_timeout(2000)
    attribute_value=page.locator("xpath=//input[@id='edit4']/ancestor::td/ancestor::tr/ancestor::table").get_attribute("id")
    print("Attribute Value of Id for Table :",attribute_value)
    page.wait_for_timeout(2000)

# 6. descendants
# Based on parent Element identify the child Element
def test_basedonparentidentifychild(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/WebTableHTML.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//table[@id='tbl1']/descendant::tr[5]/td[6]/input").fill("26000")
    page.wait_for_timeout(2000)