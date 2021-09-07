# Generated by Django 3.2.7 on 2021-09-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ImgName', models.CharField(max_length=100)),
                ('ImgURL', models.URLField()),
                ('ImgDetails', models.TextField(max_length=500)),
            ],
        ),
    ]
