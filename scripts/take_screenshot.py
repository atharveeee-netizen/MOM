from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://pubmed.ncbi.nlm.nih.gov/22425712/', wait_until='domcontentloaded')
    page.screenshot(path='docs/assets/real_fetal_risk_article.png')
    browser.close()
