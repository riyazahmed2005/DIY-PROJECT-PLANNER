from django.db import models

class DIYProject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    steps = models.TextField()
    materials = models.TextField()
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.name
