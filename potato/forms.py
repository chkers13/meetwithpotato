from django import forms
from potato.models import Post, Event
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
        'title': Textarea(attrs={'cols':60,'rows':1}),
        'data_when': Textarea(attrs={'cols':60,'rows':1}),

        }


