from utils.utils import operation_output
from utils.utils import format_from_to
from utils.utils import format_date
from utils.utils import mask_account
from utils.utils import mask_card


def test_get_executed():
    pass


def test_operation_output():
    assert operation_output({
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }, ) == "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб."
    assert operation_output({
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
            }
        },
        "description": "Перевод организации",
        "to": "Счет 64686473678894779589"
    }, ) == "26.08.2019 Перевод организации\nСчет **9589\n31957.58 руб."
    assert operation_output({
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {

            "currency": {
                "name": "руб.",
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }, ) == "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n руб."
    assert operation_output({
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }, ) == "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 "


def test_format_from_to():
    assert format_from_to(None) == ''
    assert format_from_to("Счет 12345678901234567890") == "Счет **7890"
    assert format_from_to("Название карты 1234123412341234") == "Название карты 1234 12** **** 1234"
    assert format_from_to("Название 1234123412341234") == "Название 1234 12** **** 1234"


def test_format_date():
    assert format_date(None) == ''
    assert format_date("2019-04-12T17:27:27.896421") == '12.04.2019'


def test_mask_account():
    assert mask_account("12345678901234567890") == "**7890"
    assert mask_account("невсечисла123") == "Некорректные данные"
    assert mask_account("123") == "Некорректные данные"


def test_mask_card():
    assert mask_card("1234123412341234") == "1234 12** **** 1234"
    assert mask_card("невсечисла") == "Некорректные данные"
    assert mask_card("1234567890") == "Некорректные данные"
