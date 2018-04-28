from django.db import models
from django.urls import reverse
# from model import CsvModel didn't work

class Player(models.Model):
    player_name=models.TextField(max_length=200)
    # batting_avg=models.FloatField()
    # obp=models.FloatField(blank=True)
    BRAVES="Braves"
    TIGERS="Tigers"
    TEAM_CHOICES=(
    (BRAVES,'Braves'),
    (TIGERS,'Tigers'),
    )

    team=models.CharField(choices=TEAM_CHOICES,max_length=600)
    # LEAGUE_CHOICES=(("AL","American League"),("NL","National League"),("MLB","All"))
    # league=models.CharField(choices=LEAGUE_CHOICES,max_length=600)
    player_number=models.IntegerField()
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
