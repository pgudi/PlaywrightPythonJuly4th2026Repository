from playwright.sync_api import Page, expect

def test_absolute_xpath(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=html body div form input").first.fill("demoUser1")
    page.wait_for_timeout(2000)

# Case 1: Identify Element Based on tagName
# Syntax: tagName
def test_identifyelementuisngtagname(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input").first.fill("demoUser12")
    page.wait_for_timeout(2000)
    
# Case 2: Identify Element based on tag Name with id attribute value
# Syntax: tagName#id attribute value
def test_identifyelementuisngtagnamewithidattribute(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input#pwd1pass1word1").fill("Welcome12345")
    page.wait_for_timeout(2000)

# Case 3: Identify Element based on id attribute value
# Syntax: #id attribute value
def test_identifyelementuisngidattribute(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=#pwd1pass1word1").fill("Welcome123")
    page.wait_for_timeout(2000)

# Case 4: Identify Element based on tag Name with class attribute value
# Syntax: tagName.class attribute value
def test_identifyelementuisngtagnamewithclassattribute(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input.windows").click()
    page.wait_for_timeout(2000)

# Case 5: Identify Element based on class attribute value
# Syntax: .class attribute value
def test_identifyelementuisngclassattribute(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=.windows").click()
    page.wait_for_timeout(2000)

# case 6: Identify Element based on tagName with attribute Name and Value combination
# Syntax: tagName[attributeName='attributeValue']
def test_identifyelementusingtagnamewithattributenamevalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input[id='rad1chrome']").click()
    page.wait_for_timeout(2000)

# case 7: Identify Element based on tagName with Multiple attribute Name and Value combination
# Syntax: tagName[attributeName='attributeValue'][attributeName='attributeValue']
def test_multipleattributenameandvaluecombination(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input[id='rad1chrome'][type='radio']").click()
    page.wait_for_timeout(2000)

# Case 8: Identify Element based on partial Attribute value
# Syntax:
# tagName[attributename ^= 'attributevalue']   // starts-with
# tagName[attributename $= 'attributevalue']   // ends-with
# tagName[attributename *= 'attributevalue']   // contains
def test_partialmatchingofattributevalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    #page.locator("css=input[id ^= 'chk1']").click()
    page.locator("css=input[id *= 'chk1']").click()
    page.wait_for_timeout(2000)

# Case 9: Identify Element based on tagName with attributeName combination
# Syntax:
# tagName[attributeName]
# Find Number of Links in the Application
def test_tagnamewithattributename01(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    oLinks=page.locator("css=a[href]")
    print("Number of Links in the Application :",oLinks.count())
    page.wait_for_timeout(2000)
# Display All Links Names from the Application
def test_tagnamewithattributename02(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    oLinks=page.locator("css=a[href]")
    for i in range(0, oLinks.count()):
        linkname=oLinks.nth(i).text_content()
        print("Link Name :",linkname)
    page.wait_for_timeout(2000)

# Click on Specific Link in the Application
def test_tagnamewithattributename03(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    oLinks=page.locator("css=a[href]")
    for i in range(0, oLinks.count()):
        linkname=oLinks.nth(i).text_content()
        if(linkname.startswith("S G")):
            oLinks.nth(i).click()
            break
    page.wait_for_timeout(2000)

# Case 10: Identify the Element based on nth child concept
# Syntax: nth-child(number)
def test_nthchildconcept(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=form#frm3 :nth-child(4)").fill("DemoUser4")
    page.wait_for_timeout(3000)