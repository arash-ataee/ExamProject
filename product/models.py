from hurry.filesize import size
from django.db import models
from django.core.validators import FileExtensionValidator

from store.models import Store
from user.models import Profile
from .validators import validate_file_size, price_validator


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    chasers = models.ManyToManyField(Profile, related_name='chased_categories', blank=True)
    num_chasers = models.DecimalField(max_digits=20, decimal_places=0, default=0)

    class Meta:
        ordering = ('-num_chasers',)
        indexes = [
            models.Index(fields=['name', 'id'])
        ]

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    chasers = models.ManyToManyField(Profile, related_name='chased_subcategories', blank=True)
    num_chasers = models.DecimalField(max_digits=20, decimal_places=0, default=0)

    class Meta:
        ordering = ('-num_chasers',)
        indexes = [
            models.Index(fields=['name', 'id'])
        ]

    def __str__(self):
        return self.category.name + ' - ' + self.name


def user_directory_path(instance, filename):
    return 'sender_{0}/{1}'.format(instance.sender.username, filename)


class MediaFile(models.Model):
    file = models.FileField(
        upload_to='files',
        validators=[FileExtensionValidator(['pdf', 'jpg', 'png', 'mp3', 'mp4', 'mkv']), validate_file_size],
        blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0, validators=[price_validator])
    special_users = models.ManyToManyField(
        Profile,
        related_name='bought_medias',
        related_query_name='bought_media',
        blank=True
    )

    def file_size(self):
        return size(self.file.size)

    @property
    def is_special(self):
        return False if self.price == 0 else True


class Product(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='products')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')

    subcategories = models.ManyToManyField(Subcategory, related_name='products')
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to=user_directory_path)
    caption = models.TextField(max_length=5000, blank=True)

    medias = models.ManyToManyField(MediaFile, related_name='products', blank=True)

    viewed_by = models.ManyToManyField(Profile, related_name='viewed_posts', blank=True)

    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    price = models.DecimalField(max_digits=10, decimal_places=0, default=0, validators=[price_validator])
    special_users = models.ManyToManyField(
        Profile,
        related_name='bought_products',
        related_query_name='bought_product',
        blank=True
    )

    class Meta:
        ordering = ('-create_date',)

    def __str__(self):
        return self.title


class Rate(models.Model):
    rate = models.DecimalField(max_digits=2, decimal_places=2, default=0.99)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='rates')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rates')

    class Meta:
        unique_together = ('user', 'product')
