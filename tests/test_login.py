import pytest
import softest
from pages.login import Login
from ddt import ddt, data, file_data, unpack
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
# @ddt
class TestLogin(softest.TestCase):
    log = Utils.custom_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lgn = Login(self.driver)
        self.ut = Utils()
    
    # @data(*Utils.read_data_from_csv("/home/faraz/TestFrameWork/testdata/tdatacsv.csv"))
    # @unpack
    def test_login_successful(self):
        self.lgn.login_to_website("admin@securetaxoffice.com", "A2ccX@&9")
        self.ut.assert_text("description", "description")























