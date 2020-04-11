from django.db import models

# Create your models here.
class Comment(models.Model):
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.CharField('текст комментария', max_length = 200)
    photo = models.ImageField(upload_to='user_photo/')
    
    def __str__(self):
        return self.author_name