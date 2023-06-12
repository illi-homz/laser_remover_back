from django.db import models


class Service(models.Model):
    title = models.CharField(
        verbose_name='Навзание',
        max_length=50,
        blank=False,
        default=''
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Не обязательное поле',
        blank=True,
        null=True
    )
    ordering = models.SmallIntegerField(
        verbose_name='Сортировка',
        default=1,
        blank=False
    )
    created = models.DateTimeField(
        verbose_name='Создана',
        auto_now=True,
        editable=False
    )

    def __str__(self):
        return f'{self.id} - {self.title}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
