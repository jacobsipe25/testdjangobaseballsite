from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# from model import CsvModel didn't work
class Player(models.Model):
    player_name=models.TextField(max_length=200,help_text="Player's Name")
    # batting_avg=models.FloatField()
    # obp=models.FloatField(blank=True)
    # LEAGUE_CHOICES=(("AL","American League"),("NL","National League"),("MLB","All"))
    # league=models.CharField(choices=LEAGUE_CHOICES,max_length=600)
    player_number=models.IntegerField()
    imgfile=models.ImageField(upload_to="sample/",blank=True,null=True,default="sample/noimage.png")
    # games=models.IntegerField(null=True)
    # plate_appearances=models.IntegerField(null=True)
    # at_bats=models.IntegerField(null=True)
    # runs=models.IntegerField()
    # hits=models.IntegerField()
    # doubles=models.IntegerField()
    # triples=models.IntegerField()
    # homeruns=models.IntegerField()
    # rbi=models.IntegerField()
    # sb=models.IntegerField()
    def get_absolute_url(self):
            return reverse("player_detail",kwargs={"pk":self.pk})
    def __str__(self):
        return self.player_name
class Team(models.Model):
    team_name=models.CharField(max_length=200)
    logo=models.ImageField(upload_to="teams/",blank=True,default="teams/noteam.jpg")
    user_team=User.username
    players=models.ManyToManyField(Player)
    def __str__(self):
        return self.team_name
    def get_absolute_url(self):
         return reverse("team_detail",kwargs={"pk":self.pk})
    def __str__(self):
         return self.team_name

class Game(models.Model):
    location=models.CharField(max_length=200)
    yourteam=models.ForeignKey(Team,on_delete=models.CASCADE,related_name="home")
    opponent=models.ForeignKey(Team,on_delete=models.CASCADE,related_name="away")
    date=models.DateField()
    yourscore=models.IntegerField(null=False)
    opponentscore=models.IntegerField(null=False)
    @property
    def who_won(self):
        if yourscore>opponentscore:
            return yourteam
        else:
            return opponentscore

class PlayerStats(models.Model):
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    game=models.ForeignKey(Game,on_delete=models.CASCADE)
    atbats=models.IntegerField()
    hits=models.IntegerField()
class Season(models.Model):
    season_name=models.CharField(max_length=500,null=False)
    league=models.CharField(max_length=200,null=True)
class Schedule(models.Model):
    games=models.ForeignKey(Game,on_delete=models.CASCADE)
    season_sched=models.ForeignKey(Season,on_delete=models.CASCADE)

    # @property
    # def num_walks(self):
    #     print (self.plate_appearances)

    #     print (self.at_bats)
    #     if self.plate_appearances != None and self.plate_appearances!=0 and self.at_bats != None and self.at_bats!= 0:
    #         walks=self.plate_appearances-self.at_bats
    #         return walks
    #     else:
    #         walks=0
    #         return walks
