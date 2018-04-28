from django import forms
from baseballapp.models import Player

class PlayerForm(forms.ModelForm):
    class Meta():
        model=Player
        fields='__all__'
        # widgets={
        #     "title":forms.TextInput(attrs={"class":"textinputclass"}),
        #     "text":forms.Textarea(attrs={"class":"editable postcontent"})
        # }
