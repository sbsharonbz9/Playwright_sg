from playwright.sync_api import Page, expect
import pytest


url = "https://example.com"
title_text = "Example Domain"

def url_decorator(func):

    def wrapper():
        condition = False
        if (not condition):
            url="https://google.com"
        return None
    return wrapper

@url_decorator
def test_example_title(page: Page):
    page.goto(url)
    page.screenshot(path='screenshot.png')
    page_title = page.locator("h1")
    expect(page_title).to_contain_text(title_text)

def test_link(page: Page):
    page.goto(url)
    link = page.locator("a")
    if (link.get_attribute("href") != None):
        print(link.get_attribute("href"))
    expect(link).not_to_be_empty
    link.click()
    page.screenshot(path="screenshot_stuff/next_page.png")
    