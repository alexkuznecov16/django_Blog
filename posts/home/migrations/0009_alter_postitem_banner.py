# Generated by Django 5.0.6 on 2024-05-31 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_postitem_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postitem',
            name='banner',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]
