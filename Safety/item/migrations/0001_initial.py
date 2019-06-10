# Generated by Django 2.1.5 on 2019-03-21 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('score', models.IntegerField()),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]