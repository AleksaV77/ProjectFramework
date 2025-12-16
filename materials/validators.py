from rest_framework.serializers import ValidationError

def validator_youtube(value):
    """Проверка на отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com"""

    url = "http://youtube.com"
    if value.get("video"):
            if url not in value.get("video"):
                raise ValidationError("Допускаются ссылки только на youtube")
