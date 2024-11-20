from django.db import models
from django.template.defaultfilters import slugify
import os

def save_landing_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.name:
        filename = 'Landing_Pictures/{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename)        


class Landing(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to=save_landing_image, blank=True, verbose_name='Category image')
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)     
        
def save_logo_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.name:
        filename = 'Logo/{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename)   
      
class Logo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to=save_logo_image, blank=True, verbose_name='Category image')
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)     
        

def save_videobanner(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.name:
        filename = 'Video_Banner/{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename)        


class VideoBanner(models.Model):
    video_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    video = models.FileField(upload_to=save_videobanner, verbose_name="Video",blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.video_id)
        super().save(*args, **kwargs)
        
        
class Student(models.Model):
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=10)
    email = models.EmailField()
    place = models.CharField(max_length=100)
    gen = models.CharField(max_length=50)
    status = models.TextField()
    
def save_category_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.name:
        filename = 'Category_Pictures/{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename)        
    
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to=save_category_image, blank=True, verbose_name='Category image')
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)     
 
def save_subcategory_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.name:
        filename = 'Subcategory_Pictures/{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename)        

      
class Subcategory(models.Model):
    subcategory_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    image = models.ImageField(upload_to=save_subcategory_image, blank=True, verbose_name='Subcategory image')
    desc =  models.CharField(max_length=300, null=True)
    price=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.subcategory_id)
        super().save(*args, **kwargs)