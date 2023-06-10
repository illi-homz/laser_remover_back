from django.db import models


class Illustration(models.Model):
    TATTOOS = 'tattoos'
    EYEBROW = 'eyebrow'
    EAVES = 'eaves'
    LIPS = 'lips'
    PROCESS = 'process'
    

    ILLUSTRATIONS_TYPES = [
        (TATTOOS, "Татуировки"),
        (EYEBROW, "Брови"),
        (EAVES, "Веки"),
        (LIPS, "Губы"),
        (PROCESS, "Процесс"),
    ]
    
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=50,
        default='',
        blank=False,
        help_text='Название процедуры'
    )
    count = models.IntegerField(
        verbose_name='Сеансов',
        default=0,
        blank=False,
        help_text='Количество сеансов'
    )
    type = models.CharField(
        verbose_name='Тип',
        help_text='Тип процедуры',
        max_length=10,
        choices=ILLUSTRATIONS_TYPES,
        default=TATTOOS
    )
    img = models.ImageField(
        upload_to='illustration',
        verbose_name='Изображение'
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

    @property
    def get_types(self):
        return {
            [self.TATTOOS]: 'Татуировки',
            [self.EYEBROW]: 'Брови',
            [self.EAVES]: 'Веки',
            [self.LIPS]: 'Губы',
            [self.PROCESS]: 'Процесс',
        }

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мои работы'
        verbose_name_plural = 'Мои работы'