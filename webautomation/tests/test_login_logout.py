from playwright.sync_api import Page, expect

def test_loginlogout_testcase(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    # Login caction
    page.locator("xpath=//input[@name='username']").fill("pgudi")
    page.locator("//input[@name='password']").fill("pgudi")
    page.locator("//button[normalize-space()='Sign In']").click()
    page.wait_for_timeout(3000)
    expect(page).to_have_url("https://sgtestinginstituteapp.onrender.com/home")
    # Logout Action
    page.locator("//button[normalize-space()='Logout']").click()
    page.wait_for_timeout(3000)
    expect(page).to_have_title("S G Software Testing Institute")