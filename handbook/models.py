from django.db import models


class Module(models.Model):
    """Один из четырёх модулей пособия (Математика, English, Информатика, Спецпрактикум)."""

    ACCENT_CHOICES = [
        ('math', 'Математика'),
        ('eng', 'English'),
        ('info', 'Информатика'),
        ('opt', 'Спецпрактикум'),
    ]

    number = models.PositiveSmallIntegerField(unique=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=100, help_text='Короткая подпись, например «Модуль 01 · Математика»')
    intro = models.TextField(help_text='Один-два вводных предложения под заголовком модуля')
    accent = models.CharField(max_length=10, choices=ACCENT_CHOICES)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', 'number']

    def __str__(self):
        return f'{self.number:02d}. {self.title}'


class Exercise(models.Model):
    """Задание для самостоятельной работы внутри модуля, с ключом ответа."""

    module = models.ForeignKey(Module, related_name='exercises', on_delete=models.CASCADE)
    group_label = models.CharField(
        max_length=200, blank=True,
        help_text='Заголовок подгруппы заданий, например «A. Вставьте is / are» (необязательно)',
    )
    order = models.PositiveSmallIntegerField(default=0)
    prompt = models.TextField(help_text='Текст задания')
    answer = models.TextField(
        blank=True, help_text='Ответ для самопроверки; пусто — задание открытое (например, код)',
    )

    class Meta:
        ordering = ['module', 'order']

    def __str__(self):
        return f'{self.module.title} · задание {self.order}'
