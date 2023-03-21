from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True) #record 추가할시 시간 수정
    updated_at = models.DateTimeField(auto_now=True)    #

    def __str__(self):  #java로 따지면 toString()
        return f'[{self.pk}]{self.title}'

