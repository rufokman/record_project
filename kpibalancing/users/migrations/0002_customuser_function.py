# Generated by Django 3.2.10 on 2022-09-27 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='function',
            field=models.PositiveIntegerField(choices=[(None, 'Выберите функцию'), (0, 'Экономика и финансы'), (1, 'Сооружение'), (2, 'Международные и новые бизнесы'), (3, 'Производство'), (4, 'Инвестиционная деятельность'), (5, 'Управление персоналом'), (6, 'Управление качеством'), (7, 'Генеральная инспекция'), (8, 'ФАИП и ГОЗ / КВЛ'), (9, 'Сбыт'), (10, 'Корпоративное управление, Правовое обеспечение, Управление имуществом, Непрофильные активы'), (11, 'Инновационная деятельность'), (12, 'Безопасность'), (13, 'Административное управление'), (14, 'Закупки и МТО'), (15, 'Внутренний контроль и аудит'), (16, 'Бухгалтерия')], default=0, verbose_name='Функция'),
            preserve_default=False,
        ),
    ]
