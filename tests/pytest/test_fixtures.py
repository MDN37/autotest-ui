import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("Autouse Отправляем метрику")


@pytest.fixture(scope="session")
def settings():
    print("настройки")

@pytest.fixture(scope="class")
def user():
    print("создание данных юзера, один раз на класс")

@pytest.fixture(scope="function")
def browser():
    print("открываем браузер на автотест")

class TestUserFlow:
    def test_user_can_login(self, settings, browser, user):
        ...
    def test_user_can_create_course(self, settings, browser, user):
        ...

class TestAccountFlow:
    def test_user_account(self, settings, browser, user):
        ...