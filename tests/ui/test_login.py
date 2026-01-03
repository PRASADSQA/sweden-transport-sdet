from pages.login_page import LoginPage
from data.test_users import VALID_USER

def test_user_can_login(page):
    page.goto("https://demo-ticketing.se/login")
    login = LoginPage(page)
    login.login(
        VALID_USER["username"],
        VALID_USER["password"]
    )
    assert "dashboard" in page.url