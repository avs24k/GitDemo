import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class Base_class():
    pass

    def Select_Option_BY_Text(self,locator,text):
        gender = Select(locator)
        gender.select_by_visible_text(text)

    def Select_Employee_status(self,locator,texting):
        employment_status = locator
        for S in employment_status:
            if S.text == texting:
                S.click()