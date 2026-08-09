from playwright.sync_api import Page, expect

def test_application(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    # Capture URL of Application
    url=page.url
    print("URL of the Application :",url)
    # Capture the title of Application
    title=page.title()
    print("Title of the Application :",title)
    expect(page).to_have_title("S G Software Testing Institute")
    expect(page).to_have_url("https://sgtestinginstituteapp.onrender.com/login")