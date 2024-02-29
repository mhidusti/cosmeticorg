from django.db import models



class Product_Feature(models.Model):
    title = models.CharField(max_length=200)
    content =models.CharField(max_length=200)
    attributes = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Product_Feature')
    status = models.BooleanField(default=False)
  


class Special_Products(models.Model):
    image = models.ImageField(upload_to='Special_Products',default='MenuSpecials.jpg')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    content2 = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

class Pack_Products(models.Model):
    image = models.ImageField(upload_to='Event',default='Event.jpg')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.title

    
class Gallery(models.Model):
    image = models.ImageField(upload_to='Gallery')
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name

class Social(models.Model):
    image = models.ImageField(upload_to='trainer', default='teacher.png')
    twitter = models.CharField(max_length=255, default='#')
    facebook = models.CharField(max_length=255, default='#')
    instagram = models.CharField(max_length=255, default='#')
    linkdin = models.CharField(max_length=255, default='#')
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    