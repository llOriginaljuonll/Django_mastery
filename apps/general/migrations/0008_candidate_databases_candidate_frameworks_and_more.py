# Generated by Django 4.2.4 on 2023-08-27 06:42

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_candidate_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='databases',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('MySql', 'MySql'), ('Postgree', 'MySql'), ('MongoDBSqlite3', 'MongoDBSqlite3'), ('Sqlite3', 'Sqlite3'), ('Oracle', 'Oracle'), ('Others', 'Others')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='candidate',
            name='frameworks',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Laravel', 'Laravel'), ('Angular', 'Angular')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='candidate',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Python', 'Python'), ('Javascripts', 'Javascripts'), ('Java', 'Java'), ('C++', 'C'), ('Ruby', 'Ruby'), ('Others', 'Others')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='candidate',
            name='libraries',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Ajax', 'Ajax'), ('Jquery', 'Jquery'), ('React.js', 'React.js'), ('Chart.js', 'Chart.js'), ('Gsap', 'Gsap'), ('Others', 'Others')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='candidate',
            name='mobile',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('React native', 'React native'), ('Kivy', 'Kivy'), ('Flutter', 'Flutter'), ('Ionic', 'Ionic'), ('Xamarim', 'Xamarim'), ('Others', 'Others')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='candidate',
            name='others',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('UML', 'UML'), ('SQL', 'SQL'), ('Docker', 'Docker'), ('GIT', 'GIT'), ('GraphQL', 'GraphQL'), ('Others', 'Others')], default='', max_length=50),
        ),
    ]
