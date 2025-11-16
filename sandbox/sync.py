from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    # browser = p.chromium.launch(headless=False)
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    # funny http is used in 2022
    # page.goto("http://whatsmyuseragent.org/") # ESTET reported: 	Threat: JS/Redirector.SWD trojan
    # page.goto("http://www.uitestingplayground.com/")
    page.goto("https://playwright.dev/")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="sync_example.png") # does not work or could not find the path... 
    browser.close()
