# Generated by Django 5.1.1 on 2024-12-20 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
