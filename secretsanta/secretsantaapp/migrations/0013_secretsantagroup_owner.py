# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('secretsantaapp', '0012_auto_20151201_0242'),
    ]

    operations = [
        migrations.AddField(
            model_name='secretsantagroup',
            name='owner',
            field=models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL, default=0),
            preserve_default=False,
        ),
    ]
