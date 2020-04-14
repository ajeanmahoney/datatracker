# Copyright The IETF Trust 2018-2020, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 10:52


from typing import List, Tuple      # pyflakes:ignore

from django.db import migrations, models
import django.db.models.deletion
import ietf.utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]                                   # type: List[Tuple[str]]

    operations = [
        migrations.CreateModel(
            name='BallotPositionName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
                ('blocking', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConstraintName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
                ('penalty', models.IntegerField(default=0, help_text='The penalty for violating this kind of constraint; for instance 10 (small penalty) or 10000 (large penalty)')),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContinentName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CountryName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
                ('in_eu', models.BooleanField(default=False, verbose_name='In EU')),
                ('continent', ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='name.ContinentName')),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DBTemplateTypeName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocRelationshipName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
                ('revname', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocReminderTypeName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocTagName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocTypeName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
                ('prefix', models.CharField(default='', max_length=16)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocUrlTagName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DraftSubmissionStateName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
                ('next_states', models.ManyToManyField(blank=True, related_name='previous_states', to='name.DraftSubmissionStateName')),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeedbackTypeName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FormalLanguageName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupMilestoneStateName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupStateName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupTypeName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
                ('verbose_name', models.CharField(default='', max_length=255)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImportantDateName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
                ('default_offset_days', models.SmallIntegerField()),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IntendedStdLevelName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IprDisclosureStateName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IprEventTypeName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IprLicenseTypeName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LiaisonStatementEventTypeName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LiaisonStatementPurposeName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LiaisonStatementState',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LiaisonStatementTagName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MeetingTypeName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NomineePositionStateName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewRequestStateName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewResultName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewTypeName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoleName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoomResourceName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SessionStatusName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StdLevelName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StreamName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeSlotTypeName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TopicAudienceName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
    ]
