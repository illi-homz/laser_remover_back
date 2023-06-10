from django.db import models
from django.core.validators import FileExtensionValidator


class FeedbackVideo(models.Model):
    video = models.FileField(
        verbose_name='Видео',
        upload_to='feedback_video',
        blank=False,
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True,
        default=''
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
        return f'Видео отзыв - №{self.id}'

    class Meta:
        verbose_name = 'Видео отзыв'
        verbose_name_plural = 'Видео отзывы'
