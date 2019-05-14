from django.db import models
from django.contrib.auth.models import User

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
    

