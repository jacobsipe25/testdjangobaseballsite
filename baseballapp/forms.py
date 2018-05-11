from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from baseballapp.models import Player,Team

class ContactForm(forms.Form):
    contact_address=forms.EmailField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    contact_name=forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={"class":"formcontrol"}))
    message=forms.CharField(max_length=500,widget=forms.Textarea)


class PlayerForm(forms.ModelForm):
    class Meta():
        model=Player
        fields='__all__'
        widgets={
            "player_name":forms.TextInput(attrs={"class":"formcontrol"}),
            # "text":forms.Textarea(attrs={"class":"editable postcontent"})
        }
class TeamForm(forms.ModelForm):
    class Meta():
        model=Team
        fields=("team_name","players")
        widgets={
            "team_name":forms.TextInput(attrs={"class":"formcontrol"}),
            # "text":forms.Textarea(attrs={"class":"editable postcontent"})
        }
class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta: #meta data that relates to the class
        model=User
        fields=(
        "username",
        "first_name",
        "last_name",
        "email",
        "password1",
        "password2"
        )

    def cleaned_pass(self):
        p1=self.cleaned_data["password1"]
        p2=self.cleaned_data["password2"]
        if (p1 != p2):
            raise forms.ValidationError(
            self.error_messages["password_mismatch"], code="password_mismatch"
            )
        return password2
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False) #overtides the current
        user.first_name = self.cleaned_data['first_name']#nothing can harm the web
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
