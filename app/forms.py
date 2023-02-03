from django import forms
from app.models import *
class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)

class ModelTopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


class ModelWebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['topic_name','url']
        #widgets={'name':forms.PasswordInput}
        #labels={'topic_name':'TN','name':'Na'}
        #help_texts={'name':'Only Alphabets','topic_name':'Starting Character Is Uppercase'}

class ModelAcessForm(forms.ModelForm):
    class Meta:
        model=Access_Records
        fields='__all__'
        #fields=['name']
        #exclude=['name']
        #widgets={'name':forms.PasswordInput}
        #labels={'name':'Na'}
        #help_texts={'name':'Only Alphabets'}