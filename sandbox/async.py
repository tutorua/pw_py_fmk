from playwright.async_api import async_playwright
import asyncio  
import os
import sys
import time
import datetime
import logging

async def main():
    print("Starting async playwright script...")
    
    async with async_playwright() as p:
                # browser = p.chromium.launch(headless=False)
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        # funny http is used in 2022
        # page.goto("http://whatsmyuseragent.org/") # ESTET reported: 	Threat: JS/Redirector.SWD trojan
        # page.goto("http://www.uitestingplayground.com/")
        await page.goto("https://playwright.dev/")
        await page.wait_for_load_state("networkidle") # do I need that for async mode ?
        await page.screenshot(path="acync_example.png") # does not work or could not find the path... 
        print(page.title)
        await browser.close()

asyncio.run(main())
print("Async playwright script completed.")