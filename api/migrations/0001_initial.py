# Generated by Django 4.2 on 2023-06-10 11:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Комментарий')),
                ('link', models.TextField(blank=True, default='', help_text='Ссылка на комментарий', verbose_name='Ссылка')),
                ('username', models.CharField(default='', help_text='ФИО человека оставившего отзыва', max_length=30, verbose_name='Имя')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата комментария')),
                ('ordering', models.SmallIntegerField(default=1, verbose_name='Сортировка')),
                ('created', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Текстовый отзыв',
                'verbose_name_plural': 'Текстовые отзывы',
            },
        ),
        migrations.CreateModel(
            name='FeedbackVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='feedback_video', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])], verbose_name='Видео')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Комментарий')),
                ('ordering', models.SmallIntegerField(default=1, verbose_name='Сортировка')),
                ('created', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Видео отзыв',
                'verbose_name_plural': 'Видео отзывы',
            },
        ),
        migrations.CreateModel(
            name='Illustration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', help_text='Название процедуры', max_length=50, verbose_name='Заголовок')),
                ('count', models.IntegerField(default=0, help_text='Количество сеансов', verbose_name='Сеансов')),
                ('img', models.ImageField(upload_to='illustration', verbose_name='Мои работы')),
                ('ordering', models.SmallIntegerField(default=1, verbose_name='Сортировка')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Создана')),
            ],
            options={
                'verbose_name': 'Мои работы',
                'verbose_name_plural': 'Мои работы',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(default='', verbose_name='Вопрос')),
                ('answer', models.TextField(default='', verbose_name='Ответ')),
                ('ordering', models.SmallIntegerField(default=1, verbose_name='Сортировка')),
            ],
            options={
                'verbose_name': 'Вопросы и ответы',
                'verbose_name_plural': 'Вопросы и ответы',
            },
        ),
    ]