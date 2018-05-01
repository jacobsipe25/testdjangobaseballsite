from django import forms
from baseballapp.models import Player

class PlayerForm(forms.ModelForm):
    class Meta():
        model=Player
        fields='__all__'
        widgets={
            "player_name":forms.TextInput(attrs={"class":"formcontrol"}),
            # "text":forms.Textarea(attrs={"class":"editable postcontent"})
        }
