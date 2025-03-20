from playwright.sync_api import expect, Dialog
from pages.alert_page import PlaygroundAlertPage
from pages.main_page import PlaygroundMainPage

def test_alert(browser):
    context = browser.new_context(ignore_https_errors=True, )
    page = context.new_page()
    main_page = PlaygroundMainPage(page)
    expect(main_page.alert_link).to_be_visible
    main_page.goto_alert_page()
    pa_page = PlaygroundAlertPage(page)
    expect(pa_page.alert_button).to_be_visible
    page.screenshot(path="screenshots/url_alert_page.png", full_page=True)
    pa_page.trigger_alert()
    page.on('dialog', lambda: Dialog.dismiss)
    

