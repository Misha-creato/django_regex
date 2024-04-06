

def get_fixtures():
    return [
        {
            "pattern": "[a-zA-Z]+",
            "string": "helloworld!",
            "response": "Найдено совпадение",
        },
        {
            "pattern": "\d{3}-\d{2}-\d{4}",
            "string": "hello23",
            "response": "Текст не найден",
        },
        {
            "pattern": "[a-z+",
            "string": "world!",
            "response": "Регулярное выражение неверно",
        },
    ]
