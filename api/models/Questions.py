from django.db import models


class Questions(models.Model):
    question = models.TextField(
        verbose_name='Вопрос',
        blank=False,
        default=''
    )
    answer = models.TextField(
        verbose_name='Ответ',
        blank=False,
        default=''
    )
    ordering = models.SmallIntegerField(
        verbose_name='Сортировка',
        default=1,
        blank=False
    )

    def __str__(self):
        return f'Вопрос и ответ - №{self.id}'

    class Meta:
        verbose_name = 'Вопросы и ответы'
        verbose_name_plural = 'Вопросы и ответы'