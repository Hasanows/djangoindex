from django.db import models

# Create your models here.
#bush1root
#bush1root
#bush1root
#bush1root
#bush1root
#bush1root
class Settings(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    tema = models.CharField(max_length=50, verbose_name='Тема')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

class Newave(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image1 = models.ImageField(
        upload_to="newave/",
        verbose_name='Фото 1'
    )
    image2 = models.ImageField(
        upload_to="newave/",
        verbose_name='Фото 2'
    )
    image3 = models.ImageField(
        upload_to="newave/",
        verbose_name='Фото 3'
    )


class Service(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок услуги"
    )
    description = models.TextField(
    verbose_name='Описание услуги'
    )
    image = models.ImageField(
      upload_to="services/",
      verbose_name='Изображение услуги'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Client(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя клиента'
    )
    logo = models.ImageField(
        upload_to="clients/",
        verbose_name='Логотип клиента'
    )
    website = models.URLField(
        verbose_name='Сайт клиента',
        blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Portfolio(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Название проекта'
    )
    description = models.TextField(
    verbose_name='Описание проекта'
    )
    image = models.ImageField(
    upload_to='portfolio/', verbose_name='Изображение проекта'
    )
    categories = models.CharField(
    max_length=155,
     verbose_name='Категории',
     help_text="Введите категории через запятую"
    )


    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'




#bush1root
#bush1root
#bush1root
#bush1root
#bush1root
#bush1root