# Generated by Django 2.0.3 on 2018-04-25 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseballapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='at_bats',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='doubles',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='games',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='hits',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='homeruns',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='hr',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='league',
            field=models.CharField(choices=[('AL', 'American League'), ('NL', 'National League')], default=0, max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='plate_appearances',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='rbi',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='runs',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='sb',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='triples',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.CharField(choices=[('ARI', 'Diamondbacks'), ('ATL', 'Braves'), ('BAL', 'Orioles'), ('BOS', 'Redsox'), ('CHC', 'Cubs'), ('CHW', 'Whitesox'), ('CIN', 'Reds'), ('CLE', 'Indians'), ('COL', 'Rockies'), ('DET', 'Tigers'), ('HOU', 'Astros'), ('KCR', 'Royals'), ('LAA', 'Angels'), ('LAD', 'Dodgers'), ('MIA', 'Marlins'), ('MIL', 'Brewers'), ('MIN', 'Twins'), ('NYM', 'Mets'), ('NYY', 'Yankees'), ('OAK', 'Oakland'), ('PHI', 'Phillies'), ('PIT', 'Pirates'), ('SDP', 'Padres'), ('SEA', 'Mariners'), ('SFG', 'Giants'), ('STL', 'Cardinals'), ('TBR', 'Rays'), ('TEX', 'Rangers'), ('TOT', 'Traded'), ('WSN', 'Nationals')], max_length=600),
        ),
    ]
