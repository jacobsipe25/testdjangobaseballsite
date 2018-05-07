from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from baseballapp.models import *
from django.views.generic import ListView, CreateView, DetailView,DeleteView,UpdateView
from baseballapp.forms import *
from django.urls import reverse,reverse_lazy
import logging
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.template.loader import render_to_string
from baseballstatsproj.settings import EMAIL_HOST_USER
# Create your views here
# class TeamList(ListView):
#     model=Team

def emailthemboys(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            global name
            name=request.POST["contact_name"]
            contact=request.POST["contact_address"]
            message=request.POST["message"]
            msg_tmp=render_to_string("email.txt",{"name":name,"contact":contact,"message":message})

            send_mail("New message from: "+str(name),msg_tmp,contact,[EMAIL_HOST_USER],fail_silently=False)
            send_mail("Thanks for contacting us: "+str(name),"We will be back with you ASAP.",EMAIL_HOST_USER,[contact],fail_silently=False)
            return redirect("contact_sucess")
    else:
        form=ContactForm()
    return render(request,"contact.html",{"form":form})
def success_contact(request):
    return render(request,"success.html",{"user":name})

def home(request):
    return render(request,"base.html")
def signup(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("login"))
    else:
        form = RegistrationForm()

    return render(request, 'signup.html', {'form': form})
def TeamList(request):
        player_list=Team.objects.all()
        #render takes request, aka get or post, template, context which is a dict
        #of params you pass and call by key
        return render(request,"baseballapp/team_list.html",{"team_list":team_list})
def TeamUpload(request):
    if request.method=="POST":
        form=PlayerForm(request.POST,request.FILES)
        if form.is_valid():
            newstuff=form.save(commit=False)
            newstuff.logo=request.FILES["logo"]
            newstuff.save()
            # newimage=Player(,player_name)


            return redirect(reverse("team_list"))
    else:
        form=TeamForm()
    return render(request,"baseballapp/player_form.html",{"form":form})
def PlayerUpload(request):
    if request.method=="POST":
        form=PlayerForm(request.POST,request.FILES)
        if form.is_valid():
            newstuff=form.save(commit=False)
            newstuff.imgfile=request.FILES["imgfile"]
            newstuff.save()
            # newimage=Player(,player_name)


            return redirect(reverse("player_list"))
    else:
        form=PlayerForm()
    return render(request,"baseballapp/player_form.html",{"form":form})
def PlayerList(request):
        player_list=Player.objects.all()
        #render takes request, aka get or post, template, context which is a dict
        #of params you pass and call by key
        return render(request,"baseballapp/player_list.html",{"player_list":player_list})
# class PlayerCreate(CreateView):
#     model=Player
#     form_class=PlayerForm
#     redirect_field_name="baseballapp/player_detail.html"
# def PlayerUpload(request):
#     if request.method=="POST":
#         form=PlayerForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("player_list")
#     else:
#         form=PlayerForm()
#     return render(request,"baseballapp/player_form.html",{"form":form})
class PlayerDetail(DetailView):
    model=Player
# class CreateTeam(CreateView):
#     login_url="/login/"
#     redirect_field_name="baseballapp/team_detail.html"
#     form_class=Form
#     model=Team
class TeamDetail(DetailView):
    model=Team
class PlayerUpdateView(UpdateView):
    redirect_field_name="baseballapp/player_detail.html"
    form_class=PlayerForm
    model=Player
class PlayerDeleteView(DeleteView):
    model=Player
    success_url=reverse_lazy("player_list")
def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return render(request, "baseballapp/upload_csv.html", data)
    # if not GET, then proceed
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("upload_csv"))
        #if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            return HttpResponseRedirect(reverse("upload_csv"))

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")
        #loop over the lines and save them in db. If error , store as string and then display
        for line in lines:
            print (line)
            fields = line.split(",")
            data_dict = {}
            data_dict["player_name"] = fields[0]
            data_dict["player_number"] = fields[1]
            data_dict["team"] = fields[2]
            # data_dict["league"] = fields[3]
            # data_dict["games"]=fields[4]
            # data_dict["plate_appearances"]=fields[5]
            # data_dict["at_bats"]=fields[6]
            # data_dict["runs"]=fields[7]
            # data_dict["hits"]=fields[8]
            # data_dict["doubles"]=fields[9]
            # data_dict["triples"]=fields[10]
            # data_dict["homeruns"]=fields[11]
            # data_dict["rbi"]=fields[12]
            # data_dict["sb"]=fields[13]
            # data_dict["batting_avg"]=fields[14]
            # data_dict["obp"]=fields[15]
            try:
                form = PlayerForm(data_dict)
                if form.is_valid():
                    form.save()
                else:
                    logging.getLogger("error_logger").error(form.errors.as_json())
            except Exception as e:
                logging.getLogger("error_logger").error(repr(e))
                pass

    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
        messages.error(request,"Unable to upload file. "+repr(e))

    return redirect(reverse("player_list"))
# def printthechoices():
#     fields=Player._meta.get_field("team").choices
#     return fields
# print (printthechoices())

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'registration/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('view_profile'))
        else:
            return redirect(reverse('change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'registration/change_password.html', args)
