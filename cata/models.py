from django.db import models
#for ids
import uuid
import random
import os
from django.contrib.auth.models import User

# Create your models here.


class BaseModel(models.Model):
    #default t3ml code jdid ko lmfma category jdida w edit table tkhli id ytbdl ou non
    #bigautofield tbda m 0 w fha autoincrement uuidfield securesé akther
    #example python fi terminal import uuid uuid.uuid4()
    uid = models.UUIDField(primary_key=True , default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add= True)
    updated_at = models.DateField(auto_now= True)
    category_name = models.CharField(max_length=100,null=True, blank=True)
    #nhotuh tw base l ay model akher bsh n3mluh
    class Meta:
        abstract = True

from django.contrib.auth.models import User
from django.db.models import Avg

class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True, null=True)
    def __str__(self):
        return self.name


class Article(BaseModel):
    name = models.CharField(max_length=100, null=True , blank=True)
    heading = models.CharField(max_length=350, null=True , blank=True)
    text = models.CharField(max_length=100, null=True , blank=True)
    description = models.TextField( null=True , blank=True)

    def __str__(self):
        return self.heading or "Untitled Article"
class Videomodel(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    video_file = models.FileField(upload_to='media/videos', max_length=300)
    category = models.ForeignKey(Category, related_name='videos', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name or "Untitled Video"

    def video_preview(self):
        if self.video_file:
            return format_html(
                '<video width="100" height="100" controls><source src="{}" type="video/mp4"></video>',
                self.video_file.url
            )
        return "No Video"

    video_preview.short_description = "Preview"

    def delete(self, *args, **kwargs):
        if self.video_file:
            try:
                os.remove(self.video_file.path)
            except FileNotFoundError:
                pass
        super().delete(*args, **kwargs)
from django.utils.html import format_html
class ImageModel(BaseModel):
    category = models.ForeignKey(Category, related_name='image', on_delete=models.CASCADE) 
    article = models.OneToOneField(Article, related_name='image', on_delete=models.CASCADE, null=True, blank=True) 
    image = models.FileField(upload_to='media', max_length=300)
    img_alt = models.CharField(max_length=550, blank=True)

    def __str__(self):
        return self.img_alt
    def image_preview(self):
        if self.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;"/>', self.image.url)
        return "No Image"

    image_preview.short_description = "Preview"
    def delete(self, *args, **kwargs):
        if self.image:
            try:
                os.remove(self.image.path) 
            except FileNotFoundError:
                pass  
        super().delete(*args, **kwargs)  

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} at {self.created_at}"
