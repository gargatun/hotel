# Generated by Django 4.1.5 on 2024-05-06 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='guest_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер гостя'),
        ),
    ]