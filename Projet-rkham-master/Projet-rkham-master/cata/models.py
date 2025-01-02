from django.db import models
#for ids
import uuid
import random

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


class Article(BaseModel):
    heading = models.CharField(max_length=350)
    text = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.heading

    def average_rating(self):
        avg = self.ratings.aggregate(Avg('rating')).get('rating__avg')
        return round(avg, 2) if avg else 0  

    def total_ratings(self):
        return self.ratings.count()


class Rating(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='ratings', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, f'{i} Star') for i in range(1, 6)])

    class Meta:
        unique_together = ('user', 'article')

    def __str__(self):
        return f"{self.user.username} - {self.article.heading}: {self.rating} Stars"


class ImageModel(BaseModel):
    category = models.OneToOneField(Article, related_name='image', on_delete=models.CASCADE)  # One-to-one relationship
    image = models.FileField(upload_to='media', max_length=300)
    img_alt = models.CharField(max_length=550, blank=True)

    def __str__(self):
        return self.img_alt
