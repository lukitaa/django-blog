from pagedown.widgets import AdminPagedownWidget
from django import forms
from blog.models import Article

class ArticleForm(forms.ModelForm):
    text = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Article
        fields = '__all__'
        exclude = None
