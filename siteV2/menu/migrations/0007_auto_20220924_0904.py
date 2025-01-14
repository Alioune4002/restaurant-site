# Generated by Django 3.2.15 on 2022-09-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_rename_nouveaux_plats_nouveaux_plat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='nouveaux_plat',
            name='Identifiant_plat',
        ),
        migrations.AddField(
            model_name='nouveaux_plat',
            name='categorie',
            field=models.ManyToManyField(related_name='Objet', to='menu.Categorie'),
        ),
    ]
