from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from baseballapp.models import *
from django.views.generic import ListView, CreateView, DetailView,DeleteView,UpdateView
from baseballapp.forms import PlayerForm
from django.urls import reverse,reverse_lazy
import logging
from django.contrib import messages
# Create your views here
# class TeamList(ListView):
#     model=Team
def home(request):
    return render(request,"base.html")
def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
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
