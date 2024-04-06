import re
from django.http import QueryDict


class RegexMatchService:
    @staticmethod
    def check_regex_and_get_response(pattern: str, string: str):
        response = 'Текст не найден'
        match = None

        try:
            valid_pattern = re.compile(pattern)
        except re.error:
            response = 'Регулярное выражение неверно'
        else:
            match = valid_pattern.match(string=string)

        if match is not None:
            response = 'Найдено совпадение'

        return response
