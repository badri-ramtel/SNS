from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class About(models.Model):
    about_content = RichTextField(null= False, blank= False)

    def __self__(self):
        return self.about_content
    
    class Meta:
        db_table = 'About SNS'
        verbose_name_plural = 'About SNS'


class Vision(models.Model):
    vision_content = RichTextField(null= False, blank= False)

    def __self__(self):
        return self.vision_content
    
    class Meta:
        db_table = 'Vision'
        verbose_name_plural = 'Vision'


class Term(models.Model):
    term_content = RichTextField(null= False, blank= False)

    def __self__(self):
        return f'{self.term_content}'
    
    class Meta:
        db_table = 'Terms and Condition'
        verbose_name_plural = 'Terms and Condition'