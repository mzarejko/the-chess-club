# Generated by Django 3.1.2 on 2021-05-18 11:32

import django.contrib.postgres.fields
from django.db import migrations, models
import games.chessPos


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20210516_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blackchessboard',
            name='bishops',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=games.chessPos.get_black_bishops, max_length=2, size=None),
        ),
        migrations.AlterField(
            model_name='blackchessboard',
            name='king',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=games.chessPos.get_black_king, max_length=1, size=None),
        ),
        migrations.AlterField(
            model_name='blackchessboard',
            name='knights',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=games.chessPos.get_black_knights, max_length=2, size=None),
        ),
        migrations.AlterField(
            model_name='blackchessboard',
            name='pawns',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=games.chessPos.get_black_pawns, max_length=8, size=None),
        ),
        migrations.AlterField(
            model_name='blackchessboard',
            name='queen',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=games.chessPos.get_black_queen, max_length=1, size=None),
        ),
        migrations.AlterField(
            model_name='blackchessboard',
            name='rooks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=games.chessPos.get_black_rooks, max_length=2, size=None),
        ),
        migrations.AlterField(
            model_name='whitechessboard',
            name='bishops',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=games.chessPos.get_black_bishops, max_length=2, size=None),
        ),
        migrations.AlterField(
            model_name='whitechessboard',
            name='king',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=games.chessPos.get_white_king, max_length=1, size=None),
        ),
        migrations.AlterField(
            model_name='whitechessboard',
            name='knights',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=games.chessPos.get_white_knights, max_length=2, size=None),
        ),
        migrations.AlterField(
            model_name='whitechessboard',
            name='pawns',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=games.chessPos.get_white_pawns, max_length=8, size=None),
        ),
        migrations.AlterField(
            model_name='whitechessboard',
            name='queen',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=games.chessPos.get_white_queen, max_length=1, size=None),
        ),
        migrations.AlterField(
            model_name='whitechessboard',
            name='rooks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=games.chessPos.get_white_rooks, max_length=2, size=None),
        ),
    ]