import allure

@allure.step("Opening browser")
def open_browser():
    with allure.step("Get browser"):
        ...
    with allure.step("Start browser"):
        ...

@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    ...

@allure.step("Close browser")
def close_browser():
    ...

def test_feature():
    open_browser()

    create_course(title = "Locust")
    create_course(title = "Pytest")
    create_course(title = "Python")
    create_course(title = "playwright")

    close_browser()