from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        labels = {
            'content': ''
        }
        widgets = {
            'content' : forms.Textarea(
                attrs={
                    'class': 'form-control writearea',
                    'rows': 15,
                    'placeholder': '내용을 입력하세요.',
                }
            )
        }