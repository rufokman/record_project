# Generated by Django 3.2.10 on 2022-09-26 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.PositiveIntegerField(choices=[(None, 'Выберите организацию'), (0, 'ЦА'), (1, 'Балаковская АЭС'), (2, 'Белоярская АЭС'), (3, 'Билибинская АЭС'), (4, 'Калининская АЭС'), (5, 'Кольская АЭС'), (6, 'Курская АЭС'), (7, 'Ленинградская АЭС'), (8, 'Нововоронежская АЭС'), (9, 'Ростовская АЭС'), (10, 'Смоленская АЭС'), (11, 'ПАТЭС'), (12, 'Технологический филиал'), (13, 'ОДИЦ ВВЭР'), (14, 'ОДИЦ РБМК'), (15, 'Строящаяся Балтийская АЭС'), (16, 'ИЦ Аккую'), (17, 'Воронежская АСТ'), (18, 'Филиал в Бангладеш'), (19, 'Атомтехэнерго'), (20, 'АтомЭнергоСбыт'), (21, 'АтомЭнергоРемонт'), (22, 'ЗАЭС'), (23, 'АтомТеплоЭлектроСеть'), (24, 'Техническая Академия'), (25, 'ИКАО'), (26, 'НИЦ АЭС'), (27, 'ЭНИЦ'), (28, 'Энергоатоминвест'), (29, 'Балтийская АЭС, АО'), (30, 'Атомтранс'), (31, 'Атомтеплосбыт'), (32, 'ВНИИАЭС'), (33, 'Титан - 2'), (34, 'Консист - ОС'), (35, 'С - Плюс'), (36, 'Неорганические сорбенты'), (37, 'АТОМДАТА'), (38, 'Атомдата - Центр'), (39, 'Атомдата - Иннополис')])),
                ('function', models.PositiveIntegerField(choices=[(None, 'Выберите функцию'), (0, 'Экономика и финансы'), (1, 'Сооружение'), (2, 'Международные и новые бизнесы'), (3, 'Производство'), (4, 'Инвестиционная деятельность'), (5, 'Управление персоналом'), (6, 'Управление качеством'), (7, 'Генеральная инспекция'), (8, 'ФАИП и ГОЗ / КВЛ'), (9, 'Сбыт'), (10, 'Корпоративное управление, Правовое обеспечение, Управление имуществом, Непрофильные активы'), (11, 'Инновационная деятельность'), (12, 'Безопасность'), (13, 'Административное управление'), (14, 'Закупки и МТО'), (15, 'Внутренний контроль и аудит'), (16, 'Бухгалтерия')])),
                ('type', models.PositiveIntegerField(blank=True, choices=[(None, 'Выберите тип КПЭ'), (0, 'Функциональный'), (1, 'Декомпозированный'), (2, 'Командный')], default=None, null=True)),
                ('action', models.PositiveIntegerField(blank=True, choices=[(None, 'Выберите необходимый тип корректировки'), (0, 'изменить'), (1, 'добавить'), (2, 'удалить')])),
                ('id_worker', models.CharField(blank=True, max_length=50)),
                ('role', models.CharField(max_length=100)),
                ('fio', models.CharField(max_length=300)),
                ('id_kpi_record', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=3000)),
                ('method', models.PositiveIntegerField(choices=[(None, 'Выберите методику расчета КПЭ'), (0, 'Дискретный'), (1, 'Непрерывный'), (2, 'Отсекающий'), (3, 'Понижающий')])),
                ('low_level', models.CharField(max_length=3000)),
                ('target_level', models.CharField(max_length=3000)),
                ('high_level', models.CharField(max_length=3000)),
                ('weight', models.IntegerField()),
                ('mover', models.CharField(max_length=3000)),
                ('path_to_doc', models.CharField(blank=True, max_length=3000)),
                ('comment', models.CharField(blank=True, max_length=3000)),
                ('comment_CA', models.CharField(blank=True, max_length=3000)),
                ('comment_AES_DO', models.CharField(blank=True, max_length=3000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'card',
                'managed': True,
            },
        ),
    ]