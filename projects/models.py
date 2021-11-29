from django.db import models

class CategoryModel(models.Model):
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class projectModel(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'

