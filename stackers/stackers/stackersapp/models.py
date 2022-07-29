from django.db import models

# Create your models here.
class Develop(models.Model):
    title = models.CharField(max_length=200) 
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='develop_image')
    date = models.DateTimeField(auto_now_add=True) # 자동으로 현재 시간 추가
    like_count = models.PositiveIntegerField(default=0)
    password = models.CharField(max_length=20,blank=True, null=True)
    def __str__(self):
        return self.title


class Brief(models.Model):
    title = models.CharField(max_length=200) 
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='brief_image')
    date = models.DateTimeField(auto_now_add=True) # 자동으로 현재 시간 추가
    like_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

        
class QnA(models.Model):
    title = models.CharField(max_length=200) 
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='QnA_image')
    date = models.DateTimeField(auto_now_add=True) # 자동으로 현재 시간 추가
    like_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

