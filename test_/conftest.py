import pytest
from Library.config import Config
from selenium import webdriver


@pytest.fixture(params=["Chrome","Edge"])
def _driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(Config.chrome_path)

    elif request.param == "Edge":
        driver = webdriver.Edge(Config.Ms_Edge)

    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    print(driver.title)
    driver.save_screenshot("test_offers.png")
    driver.close()