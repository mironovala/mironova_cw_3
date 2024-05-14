from utils.utils import get_executed
from utils.utils import operation_output
from utils.utils import format_from_to
from utils.utils import format_date
from utils.utils import mask_account
from utils.utils import mask_card


def test_get_executed():
    pass


def test_operation_output():
    pass


def test_format_from_to():
    pass


def test_format_date():
    assert format_date(None) == ''
    assert format_date('2019-04-12T17:27:27.896421') == '12.04.2019'


def test_mask_account():
    assert mask_account("12345678901234567890") == "**7890"
    assert mask_account("невсечисла123") == "Некорректные данные"
    assert mask_account("123") == "Некорректные данные"


def test_mask_card():
    assert mask_card("1234123412341234") == "1234 12** **** 1234"
    assert mask_card("невсечисла") == "Некорректные данные"
    assert mask_card("1234567890") == "Некорректные данные"