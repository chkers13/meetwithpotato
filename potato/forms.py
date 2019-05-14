from django import forms
from potato.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields ={'title','text'}



