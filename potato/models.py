from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class abstract_post(models.Model):
    text = models.CharField(max_length=255,verbose_name="Текст")
    data_create = models.DateTimeField(auto_now_add='true')
    author = models.ForeignKey(User,blank=True,null=True,verbose_name="Автор")
    
    
    class Meta:
        abstract = True
        
   
class Post(abstract_post):
    title = models.CharField(max_length=30,verbose_name="Заголовок")
    thumbnumber = models.IntegerField(default=0, help_text="Начинается с 0", verbose_name="Число лайков")
    likedone = models.ManyToManyField(User,related_name='likeforpost')    
    @models.permalink
    def get_absolute_url(self):
        return ['post-detail',(self.pk,)]
    @models.permalink
    def get_update_url(self):
        return ['post-update',(self.pk,)]
    
class Comment(abstract_post):
    post = models.ForeignKey(Post,blank=True,null=True,verbose_name="Пост")


class Event(models.Model):
    category_choice = (
        ('S', 'Sport'),
        ('H', 'Hobby'),
        ('P', 'Party'),
        ('O', 'Other')
    )
    age_limit_choice = (
       (12,12),
       (16,16),
       (18,18)
    )

    title = models.CharField(max_length=30,verbose_name="Заголовок")
    description = models.CharField(max_length=255,verbose_name="Описание")
    category = models.CharField(max_length=30,choices = category_choice, verbose_name="Категория")
    data_create = models.DateTimeField(auto_now_add='true', verbose_name="Дата создания")
    author = models.ForeignKey(User,blank=True,null=True,verbose_name="Организатор")
    participant = models.ManyToManyField(User,related_name='participantofevent')    
    thumbnumber = models.IntegerField(blank=True,null=True, verbose_name="Число участников")
    data_when = models.DateField(blank=True,null=True, verbose_name="Дата проведения")
    place = models.CharField(max_length=255,verbose_name="Место встречи")
    age_limit = models.IntegerField(choices = age_limit_choice, verbose_name="Возрастное ограничение")
    maxparticipant = models.IntegerField(blank=True,null=True, verbose_name="Максимальное число участников")
    minparticipant = models.IntegerField(blank=True,null=True, verbose_name="Минимальное число участников")
    
    @models.permalink
    def get_absolute_url(self):
        return ['event-detail',(self.pk,)]
    @models.permalink
    def get_update_url(self):
        return ['event-update',(self.pk,)]

        



class Profile(models.Model):             #профиль пользователя
    user = models.OneToOneField(User)    #пользователь
    info = models.TextField(blank=True,null=True, verbose_name="Информация о себе")            #информация о пользователя
    age = models.IntegerField(blank=True,null=, verbose_name="Возраст")          #возраст пользователя
    rating = models.FloatField(blank=True,null=True)         #рейтинг пользователя
    count = models.IntegerField(blank=True,null=True)        #количество оценивших пользователя

class Comment(abstract_post):
    event = models.ForeignKey(Event,blank=True,null=True,verbose_name="Пост")
