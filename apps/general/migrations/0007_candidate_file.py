# Generated by Django 4.2.4 on 2023-08-25 03:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_candidate_experience_candidate_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='file',
            field=models.FileField(default=datetime.datetime(2023, 8, 25, 3, 5, 26, 524726, tzinfo=datetime.timezone.utc), upload_to=''),
            preserve_default=False,
        ),
    ]
