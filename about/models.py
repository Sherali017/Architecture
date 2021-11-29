from django.db import models

class AboutModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'about'


class FeaturesModel(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField()
    long_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'feature'
        verbose_name_plural = 'features'


class ClientModel(models.Model):
    name = models.CharField(max_length=15)
    image = models.ImageField()
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'


class ProcessModel(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=255)
    long_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
         verbose_name = 'process'
         verbose_name_plural = 'processes'

class VideoModel(models.Model):
    title = models.CharField(max_length=255)
    suggestion = models.CharField(max_length=100)
    about_video = models.CharField(max_length=200)
    video = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

