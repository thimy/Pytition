# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-31 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0024_pytitionuser_petition_templates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='default_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='petition.PetitionTemplate', verbose_name='Default petition template'),
        ),
        migrations.AlterField(
            model_name='petitiontemplate',
            name='id',
            field=models.IntegerField(db_index=True, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='petitiontemplate',
            name='name',
            field=models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='pytitionuser',
            name='default_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='petition.PetitionTemplate', verbose_name='Default petition template'),
        ),
        migrations.AlterField(
            model_name='templateownership',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petition.PetitionTemplate'),
        ),
    ]
