# Generated by Django 4.2 on 2023-06-12 08:27

import api.services.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='Навзание')),
                ('description', models.TextField(blank=True, help_text='Не обязательное поле', null=True, verbose_name='Описание')),
                ('ordering', models.SmallIntegerField(default=1, verbose_name='Сортировка')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Создана')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.AlterField(
            model_name='feedbacktext',
            name='link',
            field=models.TextField(blank=True, default='', help_text='Ссылка на комментарий', validators=[api.services.validators.validate_link], verbose_name='Ссылка'),
        ),
    ]