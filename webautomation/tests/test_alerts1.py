from playwright.sync_api import Page, expect

def test_handle_alert1(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.wait_for_timeout(3000)

    page.on("dialog", lambda dialog: dialog.accept())

    page.locator("//button[normalize-space()='Click for JS Alert']").click()
    page.wait_for_timeout(3000)
    text_content=page.locator("#result").text_content()
    print("Text Content :",text_content)
    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")