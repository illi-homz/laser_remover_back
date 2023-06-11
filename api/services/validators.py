from django.core.exceptions import ValidationError
import re

def validate_link(link: str) -> bool:
    """
    Проверяет, является ли входная строка ссылкой и возвращает булево значение валидности

    Args:
        link (str): Ссылка для проверки

    Returns:
        bool: Возвращает True, если ссылка валидна, ValidationError — если ссылка не валидна
        или True если ссылка отсутствует
    """
    if not link:
        return True
    
    # Шаблон ссылки для проверки валидности
    pattern = re.compile(r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*")

    # Проверяем, соответствует ли ссылка шаблону
    match = re.match(pattern, link)

    # Возвращаем истину, если соответствует, и ложь, если не соответствует
    result = bool(match)

    if not result:
        raise ValidationError('Ссылка не валидная')
    
    return result