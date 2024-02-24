from tests import selenium_webform
from tests import heroku_formy

# Исполняемые тесты
def test_selwf_ff(firefox):
    selenium_webform.test_webform(firefox)

def test_selwf_ch(chrome):
    selenium_webform.test_webform(chrome)

def test_heroform_ff(firefox):
    heroku_formy.test_formy(firefox)

def test_heroform_ch(chrome):
    heroku_formy.test_formy(chrome)
