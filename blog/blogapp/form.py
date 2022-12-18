from django import forms
from .models import Post
from .models import Tag


class ContactForm(forms.Form):

    name= forms.CharField (label="Название")
    email=forms.EmailField (label="email")
    message = forms.EmailField(label="Сообщение")

class PostForm(forms.ModelForm):
    name = forms.CharField(label="Название", widget=forms.TextInput(attrs={"placeholder": "Name", "class":"form-control"}))

    tags =forms.ModelMultipleChoiceField(queryset=Tag.Objects.all(), widget=forms.CheckboxSelectMultiple(attrs={"class": "form-control"}))


    class Meta:
        model = Post
        # fields ='__all__'
        # fields = ("name", "category")
        exclude = ("user",)