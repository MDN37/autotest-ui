from playwright.sync_api import sync_playwright, expect
import local_settings as settings


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://iqos-alb.test.cleverbots.ru/admin/login/?next=/admin/")

    login = page.locator('//input[@id="id_username"]')
    login.fill(settings.USER)

    password_input = page.locator('//input[@id="id_password"]')
    password_input.fill(settings.PASSWORD)

    login_button = page.locator('//input[@value="Log in"]')
    login_button.click()

    context.storage_state(path='browser-iqos.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-iqos.json')
    page = context.new_page()

    page.goto("https://iqos-alb.test.cleverbots.ru/admin/auth/user/")

    add_button = page.locator('//div[@id="content-main"]//a[@class="addlink"]')
    add_button.click()

    login2 = page.locator('//input[@id="id_username"]')
    login2.fill('Auto_test')

    password_input2 = page.locator('//input[@id="id_password1"]')
    password_input2.fill('sR58Dc8z')

    password_input3 = page.locator('//input[@id="id_password2"]')
    password_input3.fill('sR58Dc8z')

    save_button = page.locator('//input[@class="default" and @value="Save"]')
    save_button.click()

    page.goto("https://iqos-alb.test.cleverbots.ru/admin/auth/user/")

    page.wait_for_timeout(5000)

    user_button = page.locator('//a[text()="Auto_test"]')
    user_button.click()

    delete_button = page.locator('//a[@class="deletelink"]')
    delete_button.click()

    sure_button = page.locator('//input[@value="Yes, I’m sure"]')
    sure_button.click()

    wrong_alert = page.locator('//li[@class="success"]')
    expect(wrong_alert).to_be_visible()
    expect(wrong_alert).to_have_text(
        'The user “Auto_test” was deleted successfully.'
    )

    page.wait_for_timeout(3000)