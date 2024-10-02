# Generated by Django 5.1.1 on 2024-10-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='dateCreated',
            new_name='date_created',
        ),
        migrations.AddField(
            model_name='task',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
