# Generated by Django 5.0.1 on 2024-02-20 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ad', models.CharField(max_length=50)),
                ('prenom_ad', models.CharField(max_length=50)),
                ('pass_ad', models.CharField(max_length=150)),
            ],
        ),
    ]