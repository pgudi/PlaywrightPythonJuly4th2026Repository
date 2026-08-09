from playwright.sync_api import Page, expect

def test_absolute_xpath(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=html/body/div/form/input").first.fill("demoUser1")
    page.wait_for_timeout(2000)

#Case 1: Identify Element based on TagName
def test_tagname(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//input").first.fill("DemoUser11")
    page.wait_for_timeout(2000)

#Case 2: Identify Element based on TagName with index
def test_tagname_index(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//input[2]").first.fill("Welcome12345")
    page.wait_for_timeout(2000)

# Case 3: Identify the Element based on tagName with attribute Name and value
def test_attributenamevalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    oSubmitButton=page.locator("xpath=//input[@value='Submit']")
    expect(oSubmitButton).to_be_visible()
    page.wait_for_timeout(2000)

def test_attributenamevalue2(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//input[@name='windows']").click()
    page.wait_for_timeout(2000)

# Case 4:  Identify the Element based on attribute Name and value
def test_attributenamevaluealone(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//*[@id='chk2linux']").click()
    page.wait_for_timeout(2000)

# Case 5: Identify the Element based on attribute value
def test_attributevaluealone(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//*[@*='chrome']").click()
    page.wait_for_timeout(2000)

# Case 6: Multiple Attribute Name and Value combination
def test_multipleattributenamevalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//input[@type='checkbox'][@name='windows']").click()
    page.wait_for_timeout(2000)

# Case 7: Multiple Attribute Name and Value combination using or operator
def test_multipleattributenamevaluewithoroperator(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//input[@type='checkbox' or @name='linus']").nth(0).click()
    page.wait_for_timeout(2000)

# Case 8: Multiple Attribute Name and Value combination using and operator
def test_multipleattributenamevaluewithandoperator(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//input[@type='checkbox' and @id='chk2linux']").click()
    page.wait_for_timeout(2000)

# Case 9: Partial Matching of Attribute Value
def test_partialattributevalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    #page.locator("xpath=//input[starts-with(@id,'pwd1')]").fill("Welcome12345")
    page.locator("xpath=//input[contains(@id,'word1')]").fill("Welcome12345")
    page.wait_for_timeout(2000)

#Case 10: tagName with Attribute Name combination
# Find Number of Links in the Application
def test_tagname_attributename(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    oLinks=page.locator("xpath=//a[@href]")
    print("Number of Links in The Application :",oLinks.count())
    page.wait_for_timeout(2000)
# display All Link Names from the Application
def test_tagname_attributename02(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    oLinks=page.locator("xpath=//a[@href]")
    for i in range(0, oLinks.count()):
        linkname=oLinks.nth(i).text_content()
        print("Link Name :",linkname)
    page.wait_for_timeout(2000)
# Click operation on Specific Link in the Application
def test_tagname_attributename03(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    oLinks=page.locator("xpath=//a[@href]")
    for i in range(0, oLinks.count()):
        linkname=oLinks.nth(i).text_content()
        if(linkname.endswith("Testing")):
            oLinks.nth(i).click()
            break
    page.wait_for_timeout(3000)

# Case 11: Based on Text Content Identify Element
def test_textcontent(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//a[text()='S G Software Testing']").click()
    page.wait_for_timeout(2000)


#Case 12: Based on normalize-space() Identify Element
def test_normalizespace(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//a[normalize-space()='S G Software Testing']").click()
    page.wait_for_timeout(2000)

#Case 13: Based on Partial Text Content Identify Element
def test_partialtextcontent(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//a[starts-with(text(),'S G')]").click()
    page.wait_for_timeout(2000)