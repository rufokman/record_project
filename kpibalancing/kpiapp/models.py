from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser


class Card(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    organization = models.PositiveIntegerField(choices=[
        (None, "Выберите организацию"),
        (0, "ЦА"),
        (1, 'Балаковская АЭС'),
        (2, 'Белоярская АЭС'),
        (3, 'Билибинская АЭС'),
        (4, 'Калининская АЭС'),
        (5, 'Кольская АЭС'),
        (6, 'Курская АЭС'),
        (7, 'Ленинградская АЭС'),
        (8, 'Нововоронежская АЭС'),
        (9, 'Ростовская АЭС'),
        (10, 'Смоленская АЭС'),
        (11, 'ПАТЭС'),
        (12, 'Технологический филиал'),
        (13, 'ОДИЦ ВВЭР'),
        (14, 'ОДИЦ РБМК'),
        (15, 'Строящаяся Балтийская АЭС'),
        (16, 'ИЦ Аккую'),
        (17, 'Воронежская АСТ'),
        (18, 'Филиал в Бангладеш'),
        (19, 'Атомтехэнерго'),
        (20, 'АтомЭнергоСбыт'),
        (21, 'АтомЭнергоРемонт'),
        (22, 'ЗАЭС'),
        (23, 'АтомТеплоЭлектроСеть'),
        (24, 'Техническая Академия'),
        (25, 'ИКАО'),
        (26, 'НИЦ АЭС'),
        (27, 'ЭНИЦ'),
        (28, 'Энергоатоминвест'),
        (29, 'Балтийская АЭС, АО'),
        (30, 'Атомтранс'),
        (31, 'Атомтеплосбыт'),
        (32, 'ВНИИАЭС'),
        (33, 'Титан - 2'),
        (34, 'Консист - ОС'),
        (35, 'С - Плюс'),
        (36, 'Неорганические сорбенты'),
        (37, 'АТОМДАТА'),
        (38, 'Атомдата - Центр'),
        (39, 'Атомдата - Иннополис')], verbose_name='Организация')
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
    type = models.PositiveIntegerField(choices=[
        (3, ''),
        (0, 'Функциональный'),
        (1, 'Декомпозированный'),
        (2, 'Командный')], blank=True, null=True, default=3, verbose_name='Тип КПЭ')
    action = models.PositiveIntegerField(choices=[
        (3, ""),
        (0, "изменить"),
        (1, "добавить"),
        (2, "удалить")], blank=True, default=3, verbose_name='Корректировка')
    id_worker = models.CharField(max_length=50, blank=True, verbose_name='ID сотрудника')
    role = models.CharField(max_length=100, verbose_name='Название должности')
    fio = models.CharField(max_length=300, verbose_name='ФИО')
    id_kpi_record = models.IntegerField(blank=True, null=True, verbose_name="ID КПЭ в ИС РЕКОРД")
    name = models.CharField(max_length=3000, verbose_name='Наименование КПЭ')
    method = models.PositiveIntegerField(choices=[
        (None, 'Выберите методику расчета КПЭ'),
        (0, "Дискретный"),
        (1, "Непрерывный"),
        (2, "Отсекающий"),
        (3, "Понижающий")], verbose_name='Методика расчета')
    low_level = models.CharField(max_length=3000, verbose_name="Нижний уровень")
    target_level = models.CharField(max_length=3000, verbose_name="Целевой уровень")
    high_level = models.CharField(max_length=3000, verbose_name="Верхний уровень")
    weight = models.IntegerField(verbose_name="Вес")
    mover = models.CharField(max_length=3000)
    path_to_doc = models.CharField(max_length=3000, blank=True, verbose_name='Паспорт')
    comment = models.CharField(max_length=3000, blank=True, verbose_name='Комментарий')
    comment_CA = models.CharField(max_length=3000, blank=True, verbose_name='Комментарии по аудиту (ЦА)')
    comment_AES_DO = models.CharField(max_length=3000, blank=True, verbose_name='Комментарии по аудиту (АЭС/ДО)')
    delete = models.BooleanField(default=True)
    class Meta:
        managed = True
        db_table = 'card'




