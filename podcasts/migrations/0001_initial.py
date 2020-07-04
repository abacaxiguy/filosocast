# Generated by Django 3.0.8 on 2020-07-04 12:54

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('data', models.DateTimeField(default=datetime.datetime(2020, 7, 4, 12, 54, 48, 949817, tzinfo=utc))),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='podcast_img/%Y/%m/%d')),
                ('audio', models.FileField(upload_to='podcast_audio/%Y/%m/%d')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='autores.Autor')),
            ],
        ),
    ]
