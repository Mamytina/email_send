# Generated by Django 5.0.1 on 2024-02-13 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='nom',
            new_name='nom_util',
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='prenom_util',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
