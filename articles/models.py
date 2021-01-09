from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.TextField("Назва" , max_length=200)
    article_text = models.TextField("Текст статті")
    keywords = models.CharField('Ключові слова' , max_length=120 , null = False , default = "keywords")
    imagin1 = models.ImageField("Картинка 1",upload_to='articles/' , blank=False, null=False)
    imagin2 = models.ImageField("Картинка 2",upload_to='articles/' , blank=True)
    imagin3 = models.ImageField("Картинка 3",upload_to='articles/' , blank=True)
    post_date = models.DateField("Дата публікації" , auto_now=False, auto_now_add=True)
    updated = models.DateTimeField("Редаговано" , auto_now=True, auto_now_add=False)
    author = models.ForeignKey(User , on_delete = models.CASCADE )
    link1 = models.URLField("Кнопка 1", blank=True)
    link1_name = models.TextField("Назва кнопки 1", blank=True)
    link2 = models.URLField("Кнопка 2", blank=True)
    link2_name = models.TextField("Назва кнопки 2", blank=True)
    link3 = models.URLField("Кнопка 3", blank=True)
    link3_name = models.TextField("Назва кнопки 3", blank=True)

    def __unicode__(self):
        return self.title
 
    def __str__(self):
        return self.title
 
    def get_absolute_url(self):
        return "/%s/" %(self.id)
 
    class Meta:
        ordering = ["-id", "-post_date"]
        verbose_name = "Стаття"
        verbose_name_plural = 'Статті'

class Comment(models.Model):
    article = models.ForeignKey(Article , on_delete = models.CASCADE)
    date_post = models.DateTimeField("Дата створення" , auto_now=False, auto_now_add=True)
    author = models.CharField('Імя коментатора',  max_length = 50)
    comment_text = models.CharField('Текст коментаря', max_length = 200)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = "Коментарій"
        verbose_name_plural = 'Коментарі'