from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tournament(models.Model):
    title = models.TextField("Назва" , max_length=200)
    tournament_text = models.TextField("Текст статті")
    keywords = models.CharField('Ключові слова' , max_length=120 , null = False , default = "keywords")
    imagin1 = models.ImageField("Картинка 1",upload_to='articles/' , blank=False, null=False)
    imagin2 = models.ImageField("Картинка 2",upload_to='articles/' , blank=True)
    imagin3 = models.ImageField("Картинка 3",upload_to='articles/' , blank=True)
    post_date = models.DateTimeField("Дата публікації" , auto_now=False, auto_now_add=True)
    updated = models.DateTimeField("Редаговано" , auto_now=True, auto_now_add=False)
    author = models.ForeignKey(User , on_delete = models.CASCADE )
    link1 = models.URLField("Кнопка 1", blank=True)
    link1_name = models.TextField("Назва кнопки 1", blank=True)
    link2 = models.URLField("Кнопка 2", blank=True)
    link2_name = models.TextField("Назва кнопки 2", blank=True)
    link3 = models.URLField("Кнопка 3", blank=True)
    link3_name = models.TextField("Назва кнопки 3", blank=True)
    players_osn = models.IntegerField("Кількість учасників (2-5)")
    players_dop = models.IntegerField("Кількість запасних учасників (0-2)")
    deadline_reg = models.DateTimeField('Час закінчення реєстрації')

    def __unicode__(self):
        return self.title
 
    def __str__(self):
        return self.title
 
    def get_absolute_url(self):
        return "/%s/" %(self.id)
 
    class Meta:
        ordering = ["-id", "-post_date"]
        verbose_name = "Турнір"
        verbose_name_plural = 'Турніри'

class Team(models.Model):
    tournament = models.ForeignKey(Tournament , on_delete = models.CASCADE)
    date_post = models.DateTimeField("Дата створення" , auto_now=False, auto_now_add=True)
    team_name = models.TextField("Назва команди",max_length = 100)
    capitan = models.CharField('Капітан',  max_length = 50)
    contact_capitan = models.CharField('Звязок з капітаном', max_length = 200)
    player_name_1 = models.TextField('ПІ командира (1-го учасника)')
    steam_link_1 = models.TextField('Лінк на Steam')
    vuz_1 = models.TextField('Університет')
    fuck_1 = models.TextField('Університет')
    group_1 = models.TextField('Група')
    rate_1 = models.TextField('Рейтинг')
    player_name_2 = models.TextField('ПІ 2-го учасника')
    steam_link_2 = models.TextField('Лінк на Steam')
    vuz_2 = models.TextField('Університет')
    fuck_2 = models.TextField('Університет')
    group_2 = models.TextField('Група')
    rate_2 = models.TextField('Рейтинг')
    player_name_3 = models.TextField('ПІ 3-го учасника', blank=True)
    steam_link_3 = models.TextField('Лінк на Steam', blank=True)
    vuz_3 = models.TextField('Університет', blank=True)
    fuck_3 = models.TextField('Університет', blank=True)
    group_3 = models.TextField('Група', blank=True)
    rate_3 = models.TextField('Рейтинг', blank=True)
    player_name_4 = models.TextField('ПІ 4-го учасника', blank=True)
    steam_link_4 = models.TextField('Лінк на Steam', blank=True)
    vuz_4 = models.TextField('Університет', blank=True)
    fuck_4 = models.TextField('Університет', blank=True)
    group_4 = models.TextField('Група', blank=True)
    rate_4 = models.TextField('Рейтинг', blank=True)
    player_name_5 = models.TextField('ПІ 5-го учасника', blank=True)
    steam_link_5 = models.TextField('Лінк на Steam', blank=True)
    vuz_5 = models.TextField('Університет', blank=True)
    fuck_5 = models.TextField('Університет', blank=True)
    group_5 = models.TextField('Група', blank=True)
    rate_5 = models.TextField('Рейтинг', blank=True)
    player_name_6 = models.TextField('ПІ запасного учасника 1', blank=True)
    steam_link_6 = models.TextField('Лінк на Steam', blank=True)
    vuz_6 = models.TextField('Університет', blank=True)
    fuck_6 = models.TextField('Університет', blank=True)
    group_6 = models.TextField('Група', blank=True)
    rate_6 = models.TextField('Рейтинг', blank=True)
    player_name_7 = models.TextField('ПІ запасного учасника 2', blank=True)
    steam_link_7 = models.TextField('Лінк на Steam', blank=True)
    vuz_7 = models.TextField('Університет', blank=True)
    fuck_7 = models.TextField('Університет', blank=True)
    group_7 = models.TextField('Група', blank=True)
    rate_7 = models.TextField('Рейтинг', blank=True)



    def __str__(self):
        return self.capitan

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = 'Команди'
