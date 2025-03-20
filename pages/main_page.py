from playwright.sync_api import Page

class PlaygroundMainPage:

    def __init__(self, page: Page):
        self.page = page
        self.alert_link = page.locator("a", has_text="Alerts")

    def goto_alert_page(self):
        self.page.goto("https://uitestingplayground.com")
        self.page.screenshot(path="screenshots/main.png")
        self.alert_link.click()
    
