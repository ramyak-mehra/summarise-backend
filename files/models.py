from django.db import models
# Create your models here.


class InputFile(models.Model):
    input_file = models.FileField(upload_to='input_files' , blank=True , null=True)
    input_name = models.CharField(max_length=100)

    def __str__(self):
        return self.input_name

