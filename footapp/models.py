from django.db import models

positions = {'GK': 'Goalkeeper', 'DF': 'Defender', 'MF': 'Midfielder', 'FW': 'Forward'}

class Clubs(models.Model):
    club_name = models.CharField(max_length=100)
    club_country = models.CharField(max_length=100)
    club_city = models.CharField(max_length=100)
    club_stadium = models.CharField(max_length=100)
    club_capacity = models.IntegerField()
    club_coach = models.CharField(max_length=100)


class Players(models.Model):
    player_name = models.CharField(max_length=100)
    player_position = models.CharField(max_length=2, choices=positions.items())
    player_number = models.IntegerField()
    player_club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    player_country = models.CharField(max_length=100)


