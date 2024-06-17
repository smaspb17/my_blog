from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, label='Ваше имя')
    email = forms.EmailField(label='Ваш E-mail')
    to = forms.EmailField(label='E-mail получателя')
    comments = forms.CharField(required=False, widget=forms.Textarea, label='Комментарий')
