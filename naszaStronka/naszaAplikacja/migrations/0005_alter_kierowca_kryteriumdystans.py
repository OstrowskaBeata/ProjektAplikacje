# Generated by Django 4.1.2 on 2022-12-07 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naszaAplikacja', '0004_alter_kierowca_kryteriumladunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kierowca',
            name='kryteriumDystans',
            field=models.CharField(max_length=60),
        ),
    ]
