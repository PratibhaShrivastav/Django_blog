from blogapp.models import Post,comments
from django import forms

class Post_form(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('author','title','text',)
        


class comment_form(forms.ModelForm):
    
    class Meta:
        model = comments
        fields = ('author','text')




