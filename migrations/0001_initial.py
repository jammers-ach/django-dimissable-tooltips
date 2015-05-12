# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DissmissableToolTip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unique_id', models.SlugField(help_text=b'A string, with no spaces, e.g. help-page-add-user', unique=True, max_length=100, verbose_name=b'Unique ID')),
                ('text', models.TextField(help_text=b'Html text for this tooltip, e.g. &lt;b&gt;User&ltb&gt; date of birth', verbose_name=b'Tooltip text')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HasSeen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtt', models.ForeignKey(to='django_dismissable_tooltips.DissmissableToolTip')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
