from django.db import models
from api.services.validators import validate_link
from django.core.validators import URLValidator

class FeedbackText(models.Model):
    content = models.TextField(
        verbose_name='Комментарий',
        blank=False
    )
    link = models.TextField(
        verbose_name='Ссылка',
        help_text='Ссылка на комментарий',
        default='',
        blank=True,
        # validators=[]
        validators=[validate_link]
    )
    username = models.CharField(
        verbose_name='Имя',
        help_text='ФИО человека оставившего отзыва',
        max_length=30,
        default='',
        blank=False,
    )
    date = models.DateField(
        verbose_name='Дата комментария',
        auto_now=True,
        blank=False
    )
    ordering = models.SmallIntegerField(
        verbose_name='Сортировка',
        default=1,
        blank=False
    )
    created = models.DateField(
        auto_now=True,
        editable=False
    )

    def __str__(self):
        return f'{self.id}. {self.username} [коммент: {self.content[:25]}...] - {self.date}'

    class Meta:
        verbose_name = 'Текстовый отзыв'
        verbose_name_plural = 'Текстовые отзывы'
