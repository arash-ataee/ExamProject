# Generated by Django 3.0.4 on 2020-03-29 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20200329_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='medias',
            field=models.ManyToManyField(blank=True, related_name='products', to='product.MediaFile'),
        ),
    ]
