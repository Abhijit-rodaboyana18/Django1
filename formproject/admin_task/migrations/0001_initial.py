# Generated by Django 3.2.5 on 2021-07-22 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=20)),
                ('e_id', models.IntegerField()),
                ('email', models.EmailField(max_length=20)),
                ('pas', models.CharField(max_length=20)),
            ],
        ),
    ]
