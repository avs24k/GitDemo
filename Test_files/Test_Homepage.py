import time
from Test_files.BaseFile import Base_class
from Utillities.loggig import classname
from object.HomePage import Homepage
import configparser
config = configparser.ConfigParser()
config.read("Utillities/Input.properties")


class Test_Page(Base_class,classname):

    def test_page001(self):
        log = self.getlogs()
        Hp = Homepage(self.driver)

        Hp.User_Name_Click()
        log.info("User Successfully click on Name")

        Hp.User_Name_Type(config.get("User_Info", "First_name"))
        log.info("User Successfully Type Name")

        Hp.User_Email_Click()
        log.info("User Successfully click on Email")

        Hp.User_Email_Type(config.get("User_Info", "User_Email"))
        log.info("User Successfully Type Email")

        Hp.User_Password_Click()
        log.info("User Successfully click on PassWord")

        Hp.User_Password_Type(config.get("User_Info", "User_Password"))
        log.info("User Successfully Type PassWord")

        Hp.User_checBox_click()
        log.info("User Successfully click on CheckBox")

        self.Select_Option_BY_Text(Hp.User_Select_Dropdown(), "Female")
        log.info("User Successfully click on Gander")

        time.sleep(2)
        self.Select_Employee_status(Hp.User_Emp_Status(),"Employed")
        log.info("User Successfully click on CheckBox")

        time.sleep(2)
        Hp.User_DOB("16/09/1994")
        log.info("User Successfully Type DOB")

        Hp.User_Submit_click()
        log.info("User Successfully click on Button")

        time.sleep(3)
        success_msg = Hp.User_Succussfully_Loggedin()
        assert "Success! The Form has been submitted successfully!." in success_msg
        log.critical("User Successfully logged in")

