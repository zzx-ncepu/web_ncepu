# Generated by Django 2.1.2 on 2019-05-06 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('user', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
                ('sex', models.CharField(max_length=32)),
                ('school', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
            ],
        ),
    ]
