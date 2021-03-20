# Generated by Django 3.1.6 on 2021-03-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_noteitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='noteitem',
            name='important',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='important',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]