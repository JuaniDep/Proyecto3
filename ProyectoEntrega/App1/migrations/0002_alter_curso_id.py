# Generated by Django 4.1.7 on 2023-03-08 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
