import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize(
    'number',
    [
        1,
        2,
        3,
        -1
    ]
)
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize(
    'number, expected',
    [
        (1, 1),
        (2, 4),
        (3, 9),
        (4, 16)
    ]
)
def test_numbers_several(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('browser', ['chromium', 'firefox', 'webkit'])
@pytest.mark.parametrize('os', ['macos', 'linux', 'windows', 'debian'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0



@pytest.fixture(params=['chromium', 'firefox', 'webkit'])
def browser(request: SubRequest):
    return request.param

def test_open_browser(browser: str):
    print(f'Running test on browser, {browser}')

@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperation:
    @pytest.mark.parametrize("account", ["Credit card", "Debit card"])
    def test_user_with_operation(self, user: str, account: str):
        print(f"User with operations: {user}")

    def test_user_without_operation(self, user: str):
        print(f"User with operations: {user}")

users = {
'+555555555':'user with money',
'+666666666': 'user with phone',
'+777777777' : 'user with no money'
}

@pytest.mark.parametrize(
    'phone_numbers',
    users.keys(),
    ids =  lambda phone_numbers: f'{phone_numbers}: {users[phone_numbers]}'
)
def test_identifiers(phone_numbers: str):
    ...