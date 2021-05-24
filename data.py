"""Работа с данные напоминаний - добавление, удаление"""
import re
from typing import NamedTuple


class Message(NamedTuple):
    """Структура рассшаренного сообщения о добавлении напоминания"""
    name: str
    hours: int
    minutes: int
    day: int
    month: int


def parse_message(message: str): # -> Message:
    """Парсит пришедшее сообщение с данными о напоминании"""
    regexp_result = re.match(r"(.+)[ ](\d\d)[:](\d\d) (\d\d) (\d\d)", message)
    if regexp_result:
        print(regexp_result.group(1))
        print(regexp_result.group(2))
        print(regexp_result.group(3))
        print(regexp_result.group(4))
        print(regexp_result.group(5))
    else:
        print("No")