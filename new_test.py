from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_fill = page.get_by_test_id('login-form-email-input').locator('input')
    expect(email_fill).to_be_visible()

    pass_fill = page.get_by_test_id('login-form-password-input').locator('input')
    expect(pass_fill).to_be_visible()

    login_fill = page.get_by_test_id('login-page-login-button')
    expect(login_fill).to_be_visible()

    reg_button = page.get_by_test_id('login-page-registration-link')
    reg_button.click()

    email_fill2 = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(email_fill2).to_be_visible()

    pass_fill2 = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(pass_fill2).to_be_visible()

    reg_fill2 = page.get_by_test_id('registration-page-registration-button')
    expect(reg_fill2).to_be_visible()

    page.wait_for_timeout(3000)
