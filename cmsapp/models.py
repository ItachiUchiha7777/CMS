from django.db import models
import uuid
from profiles.models import UserProfile
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    writer=models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True,blank=True)
    title=models.CharField( max_length=500)
    image=models.ImageField(upload_to="img")
    body=RichTextField()
    post_id = models.UUIDField(default=uuid.uuid4(), primary_key=True, unique=True, editable=False)
    created=models.DateTimeField(auto_now_add=True)
    modefield=models.DateTimeField(auto_now=True)
    slug=models.SlugField()
    category=models.ForeignKey("Category",on_delete=models.SET_NULL,blank=True,null=True)
    
    def __str__(self):
        return self.title
class Category(models.Model):
    title=models.CharField(max_length=100)
    category_id=models.UUIDField(default=uuid.uuid4(),primary_key=True,unique=True,editable=False)
    slug=models.SlugField()
    
    def __str__(self):
        return self.title
    
