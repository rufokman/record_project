from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):

    function = models.PositiveIntegerField(choices=[
        (None, 'Выберите функцию'),
        (0, "Экономика и финансы"),
        (1, "Сооружение"),
        (2, "Международные и новые бизнесы"),
        (3, "Производство"),
        (4, "Инвестиционная деятельность"),
        (5, "Управление персоналом"),
        (6, "Управление качеством"),
        (7, "Генеральная инспекция"),
        (8, "ФАИП и ГОЗ / КВЛ"),
        (9, "Сбыт"),
        (10, "Корпоративное управление, Правовое обеспечение, Управление имуществом, Непрофильные активы"),
        (11, "Инновационная деятельность"),
        (12, "Безопасность"),
        (13, "Административное управление"),
        (14, "Закупки и МТО"),
        (15, "Внутренний контроль и аудит"),
        (16, "Бухгалтерия")], verbose_name='Функция')



    # add additional fields in here