from django import forms

from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    text = forms.CharField(label='内容', widget=forms.Textarea())
    image = forms.ImageField(label='イメージ画像', required=False) 

class ContactForm(forms.Form):
    subject = forms.CharField(label='お名前', max_length=100)
    sender = forms.EmailField(label='メールアドレス', help_text='※ご確認の上、正しく入力してください。')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea())
    myself = forms.BooleanField(label='同じ内容を受け取る', required=False)

