import time
import re
from collections import OrderedDict


def data_validator(date: str) -> str | bool:
    """
    Валидатор для даты;
    Возаращает 'data', при успешной валидации,
    в ином случае False.
    """
    try:
        _ = time.strptime(date, '%d.%m.%Y')
        return 'data'
    except ValueError:
        try:
            _ = time.strptime(date, '%d-%m-%Y')
            return 'data'
        except ValueError:
            return False


def phone_validator(phone: str) -> str | bool:
    """
    Валидатор для номера телефона;
    Возаращает 'phone', при успешной валидации,
    в ином случае False.
    """
    mask = re.compile(r'^\+(?:|\d)[\d\ ]{10,10}\d')
    if mask.search(phone.replace(' ', '')):
        return 'phone'
    return False


def email_validator(email: str) -> str | bool:
    """
    Валидатор для электронной почты';
    Возаращает 'email', при успешной валидации,
    в ином случае False.
    """
    if bool(re.fullmatch("[a-zA-Z0-9.]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+", email)):
        return 'email'
    return False


# Упорядоченный словарь с валидаторами в порядке дата -> телефон -> почта.
validators = OrderedDict([
    ('date', data_validator),
    ('phone', phone_validator),
    ('email', email_validator)
])
