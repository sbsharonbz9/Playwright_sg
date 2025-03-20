from playwright.sync_api import Page

class PlaygroundAlertPage:

    def __init__(self, page: Page):
        self.page = page
        self.alert_button = page.locator("#alertButton")
        self.confirm_button = page.locator("#confirmButton")
        self.prompt_button = page.locator("#promptButton")

    def goto(self):
        self.page.goto("https://uitestingplayground.com/alerts")
    
    def trigger_alert(self):
        self.alert_button.click()
