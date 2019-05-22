from django import forms
from django.contrib.auth.models import User
from potato.models import Post, Event, Profile
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.forms import  Textarea
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields ={'title','text'}



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields ={'title','description','category','age_limit','place','data_when','minparticipant','maxparticipant'}
        labels ={
            "title": "Rule Title",
            'description':"refjefjiop"
        }

        widgets = {
        'description': Textarea(attrs={'cols':60,'rows':5}),



        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields ={'first_name','last_name','email'}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields ={'info','age'}