from django.db import models


positions = {'GK': 'Goalkeeper', 'DF': 'Defender', 'MF': 'Midfielder', 'FW': 'Forward'}

class Clubs(models.Model):
    club_name = models.CharField(max_length=100)
    club_country = models.CharField(max_length=100)
    club_city = models.CharField(max_length=100)
    club_stadium = models.CharField(max_length=100)
    club_capacity = models.IntegerField()
    club_coach = models.CharField(max_length=100)
    club_logo = models.ImageField(upload_to='club_logos/', null=True, blank=True)

    def __str__(self):
        return self.club_name

class Players(models.Model):
    player_name = models.CharField(max_length=100)
    player_position = models.CharField(max_length=2, choices=positions.items())
    player_number = models.IntegerField()
    player_club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    player_country = models.CharField(max_length=100)
    player_photo = models.ImageField(upload_to='player_photos/', null=True, blank=True)

    def __str__(self):
        return self.player_name

