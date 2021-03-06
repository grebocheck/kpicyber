from django.db import models
from articles.models import Article

class Abou(models.Model):
    about_text = models.TextField("Текст")
    class Meta:
        verbose_name = "Про сайт"
        verbose_name_plural = 'Про сайт'

class Contact(models.Model):
    contact_text = models.TextField("Текст")
    class Meta:
        verbose_name = "Контакти"
        verbose_name_plural = 'Контакти'

class Imagin(models.Model):
    imagin_url = models.URLField("адреса картинки")
    title = models.TextField("Назва")
    texte = models.TextField("Текст")
    bath_title = models.TextField("Текст кнопки")
    batn_url = models.URLField("Адреса для кнопки")

    class Meta:
        verbose_name = "Картинка на прокрутці"
        verbose_name_plural = 'Картинки на прокруці'

class Topx(models.Model):
    top_article = models.ForeignKey(Article , on_delete = models.CASCADE)
    class Meta:
        verbose_name = "Стаття на головній"
        verbose_name_plural = 'Статті на головній'

class Downl(models.Model):
    filer = models.FileField(upload_to='files')
    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = 'Файли'
