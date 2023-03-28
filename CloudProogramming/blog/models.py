import os.path

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    create_at = models.DateTimeField(auto_now_add=True) #record 추가할시 시간 수정
    updated_at = models.DateTimeField(auto_now=True)    #

    def __str__(self):  #java로 따지면 toString()
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)      #파일의 이름을 basename만 잘라서 보여주기 위해
