# Generated by Django 3.0 on 2020-03-24 14:48

from django.conf import settings
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('num_chasers', models.DecimalField(decimal_places=0, default=0, max_digits=20)),
                ('chasers', models.ManyToManyField(blank=True, related_name='chased_categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-num_chasers',),
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('num_chasers', models.DecimalField(decimal_places=0, default=0, max_digits=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='product.Category')),
                ('chasers', models.ManyToManyField(blank=True, related_name='chased_subcategories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-num_chasers',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('cover', models.ImageField(upload_to=product.models.user_directory_path)),
                ('caption', models.TextField(blank=True, max_length=5000)),
                ('image', models.ImageField(upload_to=product.models.user_directory_path)),
                ('pdf', models.FileField(blank=True, upload_to=product.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('audio', models.FileField(blank=True, upload_to=product.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(['mp3'])])),
                ('video', models.FileField(blank=True, upload_to=product.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(['mp4'])])),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('rate_p', models.DecimalField(decimal_places=2, default=0.99, max_digits=2)),
                ('create_date', models.DateTimeField()),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='store.Store')),
                ('rated_by', models.ManyToManyField(blank=True, related_name='rated_posts', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('subcategories', models.ManyToManyField(related_name='posts', to='product.Subcategory')),
                ('viewed_by', models.ManyToManyField(blank=True, related_name='viewed_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-rate_p',),
            },
        ),
        migrations.AddIndex(
            model_name='subcategory',
            index=models.Index(fields=['name', 'id'], name='product_sub_name_1de660_idx'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name', 'id'], name='product_cat_name_88a6b7_idx'),
        ),
    ]
