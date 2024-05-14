import json


def get_executed():
    with open("operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    items = [payment for payment in data if payment.get("state") == "EXECUTED"]
    items.sort(key=lambda x: x.get("date"), reverse=True)
    return items


def operation_output(item):
    date = format_date(item.get("date"))
    descr = item.get("description")
    cart_from = format_from_to(item.get("from"))
    account_to = format_from_to(item.get("to"))
    amount = item.get("operationAmount").get("amount")
    currency = item.get("operationAmount").get("currency").get("name")

    if cart_from:
        cart_from += ' -> '
    else:
        cart_from = ''
    if amount is None:
        amount = ''
    if currency is None:
        currency = ''

    return f"{date} {descr}\n{cart_from}{account_to}\n{amount} {currency}"


def format_date(date):
    if date is None:
        return ''
    else:
        date_raw = date[0:10].split(sep="-")
        return f"{date_raw[2]}.{date_raw[1]}.{date_raw[0]}"


def format_from_to(number):
    if number is None:
        return ""

    msg = number.split()

    if msg[0] == "Счет":
        return f"{msg[0]} {mask_account(msg[-1])}"
    else:
        if len(msg) == 3:
            return f"{msg[0]} {msg[1]} {mask_card(msg[-1])}"
        else:
            return f"{msg[0]} {mask_card(msg[-1])}"


def mask_account(number: str):
    if number.isdigit() and len(number) > 4:
        return f"**{number[-4:]}"
    else:
        return "Некорректные данные"


def mask_card(number: str):
    if number.isdigit() and len(number) == 16:
        return f"{number[0:4]} {number[4:6]}** **** {number[-4:]}"
    else:
        return "Некорректные данные"
