# Generated by Django 5.0.6 on 2024-05-31 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_postitem_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postitem',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.jpg', upload_to=''),
        ),
    ]
