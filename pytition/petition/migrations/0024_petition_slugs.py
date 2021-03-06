# Generated by Django 2.1.5 on 2019-03-27 18:05

from django.db import migrations, models
from django.utils.text import slugify
from django.utils.html import mark_safe, strip_tags
import html


def set_my_defaults(apps, schema_editor):
    Petition = apps.get_model('petition', 'Petition')
    SlugModel = apps.get_model('petition', 'SlugModel')
    for p in Petition.objects.all():
        if p.slugs.count() == 0:
            raw_title = html.unescape(mark_safe(strip_tags(p.title).strip()))
            slug = SlugModel(slug=slugify(raw_title[:200]))
            slug.save()
            p.slugs.add(slug)
            p.save()


def unset_defaults(apps, schema_editor):
    Petition = apps.get_model('petition', 'Petition')
    for p in Petition.objects.all():
        for slug in p.slugs.all():
            slug.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0023_auto_20190327_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='slugs',
            field=models.ManyToManyField(null=True, blank=True, to='petition.SlugModel'),
        ),
        migrations.RunPython(set_my_defaults, unset_defaults),
        migrations.AlterField(
            model_name='petition',
            name='slugs',
            field=models.ManyToManyField(blank=True, to='petition.SlugModel')
        )
    ]
