from django.db import models
# from django.core.validators import FileExtensionValidator 
# Create your models here.

class Slider(models.Model):
    picture = models.ImageField(upload_to= 'images/slider/', null= False, blank= False)
    title = models.CharField(max_length= 100, null= False, blank= False)
    sub_title = models.CharField(max_length= 254, null= False, blank= False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Slider'
        verbose_name_plural = 'Slider'
        ordering = ['-id']


class President(models.Model):
    name = models.CharField(max_length= 100, null= False, blank= False)
    image = models.ImageField(upload_to= 'images/president/', null= False, blank= False)
    p_message = models.TextField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'President'
        verbose_name_plural = 'President'

class Subscribe(models.Model):
    email = models.EmailField(max_length= 254, null= False, blank= False)

    def __self__(self):
        return self.email

    class Meta:
        db_table = 'Subscribe'
        verbose_name_plural = 'Subscribe'
        ordering = ['-id']


class Adversite(models.Model):
    # content = models.FileField(upload_to='videos/advertisement/',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    image = models.ImageField(upload_to= 'images/advertise/', null= False, blank= False)
    def __str__(self):
        return f'{self.image}'
    
    class Meta:
        db_table = 'Advertisement'
        verbose_name_plural = 'Advertisement'
        ordering = ['-id']