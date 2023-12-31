# Generated by Django 4.2.4 on 2023-08-20 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_candidate_situation'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='experience',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='gender',
            field=models.CharField(default=datetime.datetime(2023, 8, 20, 15, 36, 46, 992660, tzinfo=datetime.timezone.utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='personality',
            field=models.CharField(choices=[('', 'Select a personality'), ('I am outgoing', 'I am outgoing'), ('I am sociable', 'I am sociable'), ('I am antisocial', 'I am antisocial'), ('I am discreet', 'I am discreet'), ('I am serious', 'I am serious')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='salary',
            field=models.CharField(default=datetime.datetime(2023, 8, 20, 15, 37, 14, 937509, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='smoker',
            field=models.CharField(choices=[('1', 'Yes'), ('2', 'No')], default='', max_length=3, null=True),
        ),
    ]
