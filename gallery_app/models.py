from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, null= False, blank= False)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'Category'
        verbose_name_plural = 'Category'
        ordering = ['-id']
    

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null= True, blank= True)
    image = models.ImageField(upload_to= 'images/gallery/', null= False, blank= False)
    description = models.TextField()

    def __str__(self):
        return f'{self.description}::{self.category}' 
    
    class Meta:
        db_table = 'Photo'
        verbose_name_plural = 'Photo'
        ordering = ['-id'] 