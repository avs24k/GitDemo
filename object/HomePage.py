import pytest
from selenium.webdriver.common.by import By
from Test_files.BaseFile import Base_class

class Homepage(Base_class):
    def __init__(self,driver):
        self.driver = driver

        self.Name = "form-control"
        self.Email = "email"
        self.password = "exampleInputPassword1"
        self.checkbox = "(//input[@class='form-check-input'])[1]"
        self.Gender = "exampleFormControlSelect1"
        self.Status = "//div[@class='form-check form-check-inline']"
        self.Birth = "//input[@max='3000-12-31']"
        self.Submit = "//input[@class='btn btn-success']"
        self.success = "div[class*=alert-success]"

    def User_Name_Click(self):
        self.driver.find_element(By.CLASS_NAME,self.Name).click()

    def User_Name_Type(self,getdata):
        self.driver.find_element(By.CLASS_NAME,self.Name).send_keys(getdata)

    @pytest.fixture(params=[{"First_name": "Avinash", "Second_name": "Ramesh", "Last_name": "Patil"}])
    def getdata(self, request):
        return request.param

    def User_Email_Click(self):
        self.driver.find_element(By.NAME, self.Email).click()

    def User_Email_Type(self,user_Email):
        self.driver.find_element(By.NAME, self.Email).send_keys(user_Email)

    def User_Password_Click(self):
        self.driver.find_element(By.ID, self.password).click()

    def User_Password_Type(self,use_password):
        self.driver.find_element(By.ID, self.password).send_keys(use_password)

    def User_checBox_click(self):
        self.driver.find_element(By.XPATH, self.checkbox).click()

    def User_Select_Dropdown(self):
        return self.driver.find_element(By.ID, self.Gender)

    def User_Emp_Status(self):
        return self.driver.find_elements(By.XPATH, self.Status)

    def User_DOB(self,user_dob):
        self.driver.find_element(By.XPATH, self.Birth).send_keys(user_dob)

    def User_Submit_click(self):
        self.driver.find_element(By.XPATH, self.Submit).click()

    def User_Succussfully_Loggedin(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.success).text
