# Generated by Django 3.2 on 2023-05-17 16:58

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=256)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('text', models.TextField()),
                (
                    'pub_date',
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        verbose_name='Дата добавления',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=256)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GenreTitle',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('text', models.TextField(blank=True, null=True)),
                (
                    'score',
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(10),
                        ]
                    ),
                ),
                (
                    'pub_date',
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        verbose_name='Дата добавления',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=256)),
                ('year', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                (
                    'category',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='titles',
                        to='reviews.categories',
                    ),
                ),
                (
                    'genre',
                    models.ManyToManyField(
                        through='reviews.GenreTitle', to='reviews.Genres'
                    ),
                ),
            ],
        ),
    ]
