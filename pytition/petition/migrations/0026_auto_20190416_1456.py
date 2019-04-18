# Generated by Django 2.2 on 2019-04-16 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0025_auto_20190401_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='slugname',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]