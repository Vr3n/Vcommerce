import pytest
from django.contrib.auth.models import User
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.mark.selenium
def test_dashboard_admin_login(live_server,
                               django_db_fixture_setup,
                               edge_browser_instance):

    i = User.objects.get(id=1)
    print(i.password)

    browser = edge_browser_instance

    browser.get(("%s%s" % (live_server.url, "/admin/login/")))

    user_name = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")

    submit = browser.find_element(
        By.XPATH, '//*[@id="login-form"]/div[3]/input')

    user_name.send_keys("admin")
    password.send_keys("password")
    submit.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source
