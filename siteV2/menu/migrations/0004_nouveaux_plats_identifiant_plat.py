from django.db import migrations, models
from django.utils import timezone
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20220923_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='nouveaux_plats',
            name='Identifiant_plat',
            # Utilisation de timezone.make_aware pour garantir que l'heure est bien en UTC
            field=models.CharField(default=timezone.make_aware(datetime.datetime(2022, 9, 23, 16, 19, 43)), max_length=200),
            preserve_default=False,
        ),
    ]