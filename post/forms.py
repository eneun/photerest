from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
        labels = {
            'content': '',
        }
        widgets={
            'content' : forms.Textarea(
                attrs={
                    'class': 'form-control writearea',
                    'rows': 15,
                    'placeholder': '내용을 입력하세요.',
                }
            )
            
        }