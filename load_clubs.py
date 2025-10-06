import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'football_proj.settings')
django.setup()

from footapp.models import Players, Clubs
from django.core.files import File

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, 'players.csv')

with open(csv_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            club = Clubs.objects.get(club_name=row['player_club'])
        except Clubs.DoesNotExist:
            print(f"⚠️ Club {row['player_club']} not found. Skipping player {row['player_name']}.")
            continue

        player, created = Players.objects.get_or_create(
            player_name=row['player_name'],
            defaults={
                'player_position': row['player_position'],
                'player_club': club,
                'player_country': row['player_country'],
                'player_number': int(row['player_number']),
            }
        )

print("\n✅ Загрузка игроков завершена!")
