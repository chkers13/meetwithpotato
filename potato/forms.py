from django import forms
from potato.models import Post, Event
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields ={'title','text'}



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields ={'title','description','category','age_limit','place','data_when','minparticipant','maxparticipant'}
        


