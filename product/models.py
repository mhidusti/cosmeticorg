from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='Products')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    attributes = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.title