# Generated by Django 4.2.5 on 2023-11-07 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Football',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Place', models.CharField(help_text='Employee ID', max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('Pskill', models.IntegerField()),
                ('age', models.IntegerField()),
                ('Jersynumber', models.IntegerField()),
            ],
        ),
    ]
