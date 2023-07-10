from django.db import models

class Blog(models.Model):
    nama_depan      = models.CharField(max_length=100)
    nama_belakang   = models.CharField(max_length=100)
    username        = models.CharField(max_length=100)
    
    def __str__(self):
        return "{}.{}".format(self.id, self.username)
